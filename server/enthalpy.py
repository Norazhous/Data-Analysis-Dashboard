from flask import Flask, jsonify, request, Response, render_template
from flask_cors import CORS
# from modules import globalVariables

from modules import R134aSimpleCycleCalculationPloting
from PIL import Image
import base64
import io
import os
import json

def getUserInformation():
     try:
        username = request.args.get('username', default='none')
        course = request.args.get('course', default='none')
        hardware = request.args.get('hardware', default='none')
        if(hardware == 'none' or course == 'none' or username == 'none'):
            return {
            "response": "ERROR", 
            "message": 'missing username, hardware or course'
            }
        else:
            return {
                "user": username, 
                "type":"response", 
                "hardware": hardware, 
                "course": course, 
                }
     except Exception as e:
            return {
                "response": "ERROR", 
                "message": str(e)
                }

# save the Json in a Json file
def saveDataFile(saveData):
    # get UUID from logging?
    # UUID = getUserInformation["user"]
    # define the name of the directory+UUID
    path = "./server/uuid/testUUID"
    # check whether directory already exists
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
    # define the name of the directory with its subdirectories
    jsonDatasave = saveData.copy()
    jsonDatasave.pop("img_data")

    if os.path.exists("./server/uuid/testUUID/testUUID_savedata1.json"):
        # 1. Read file contents
        with open("./server/uuid/testUUID/testUUID_savedata1.json", "r", encoding='utf-8') as file:
            data = json.load(file)
    # 2. Update json object
        # data.append(jsonDatasave)
        # Ensure data is a list and update json object
        if isinstance(data, list):
            data.append(jsonDatasave)
        else:
            data = [data, jsonDatasave]
    else:
        # Create new data list
        data = [jsonDatasave]
    # print(data)
    # 3. Write json file
    with open("./server/uuid/testUUID/testUUID_savedata1.json", "w", encoding='utf-8') as file:
        json.dump(data, file, indent=6)
    # file.close()

# save img in a json file


def saveImgFile(saveImg):
    # get UUID from logging?
    # UUID = getUserInformation["user"]
    # define the name of the directory +UUID
    path = "./server/uuid/testUUID"
    # check whether directory already exists
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
    jsonDatasave = saveImg.copy()
    jsonImgsave = jsonDatasave.pop("img_data")
    save_file = open("./server/uuid/testUUID/testUUID_saveimg.json", "w")
    json.dump(jsonImgsave, save_file, indent=6)
    save_file.close()


# get the img and encode it
def imgEncode():
    im = Image.open("./server/uuid/phFigure.png")
    data = io.BytesIO()
    im.save(data, "png")
    encoded_img_data = base64.b64encode(data.getvalue())
    # print(encoded_img_data.decode('utf-8'))
    return encoded_img_data.decode("utf-8")


# def createApp():
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/enthalpy", methods=["GET", "POST"])
def enthalpy():

    # getUserInformation()

    # if getUserInformation["user"] ==  "ERROR":
    #     response_object = {"status": "User Information Error"}
    # else:
        # Initialize variables
        Parameters_MeasuredData = {}
        Parameters_StudentCaculation = {}
        Parameters_SystemCaculation = {}
        Parameters_DeviationCaculation = {}
        Parameters_SaturatedValue = {}

        response_object = {"status": "success"}
        if request.method == "POST":
            post_data = request.get_json()
            if not post_data:
                response_object["status"] = "fail"
                response_object["message"] = "Invalid data received"
                return jsonify(response_object), 400

            data_type = post_data.get("dataType")
            if data_type == "MeasuredandCalculation":
                Parameters_MeasuredData.update({
                    "MeasuredTime": post_data.get("MeasuredTime"),
                    "T1": post_data.get("T1"),
                    "T2": post_data.get("T2"),
                    "T3": post_data.get("T3"),
                    "T4": post_data.get("T4"),
                    "T5": post_data.get("T5"),
                    "P1": post_data.get("P1"),
                    "P2": post_data.get("P2"),
                    "P3": post_data.get("P3"),
                    "E": post_data.get("E"),
                    "F": post_data.get("F"),
                    "ASP": post_data.get("ASP"),
                    "MeasuredDataStatus": 1,
                })
                response_object["message"] = "Parameters_MeasuredData added!"
                Parameters_StudentCaculation.update({
                    "H1_Stu": post_data.get("H1"),
                    "H2_Stu": post_data.get("H2"),
                    "H3_Stu": post_data.get("H3"),
                    "H4_Stu": post_data.get("H4"),
                    "H5_Stu": post_data.get("H5"),
                    "m_Stu": post_data.get("m"),
                    "QL_Stu": post_data.get("QL"),
                    "QH_Stu": post_data.get("QH"),
                    "W_Stu": post_data.get("W"),
                    "COP_Stu": post_data.get("COP"),
                    "n_Stu": post_data.get("n"),
                    "CalculatedDataStatus": 1,
                })
                response_object["message"] = "Parameters_StudentCaculation added!"

                data_from_moduels = R134aSimpleCycleCalculationPloting.systemCalculation(
                    Parameters_MeasuredData)
                # print(data_from_moduels)
                Parameters_SystemCaculation = data_from_moduels[0]
                Parameters_SaturatedValue = data_from_moduels[1]
                response_object["Parameters_SystemCaculation"] = Parameters_SystemCaculation
                response_object["Parameters_SaturatedValue"] = Parameters_SaturatedValue
                Parameters_DeviationCaculation = R134aSimpleCycleCalculationPloting.DeviationCalculation(
                    Parameters_StudentCaculation, Parameters_SystemCaculation)
                response_object["Parameters_DeviationCaculation"] = Parameters_DeviationCaculation
                response_object["Parameters_MeasuredData"] = Parameters_MeasuredData
                response_object["Parameters_StudentCaculation"] = Parameters_StudentCaculation
                response_object["img_data"] = imgEncode()
                saveDataFile(response_object)
                saveImgFile(response_object)

            else:
                response_object["message"] = "Data not yet complete"

            return jsonify(response_object)


    # @app.errorhandler(500)
    # def handle_server_error(error):
    #     response_object = {"status": "fail"}
    #     response_object["message"] = error
    #     print(error)
    #     return jsonify(response_object)


if __name__ == "__main__":
    app.run()

app.run(debug=True)
# return app
