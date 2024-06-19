from flask import Flask, jsonify, request, Response, render_template
from flask_cors import CORS
from app_globalVal import (
    Parameters_MeasuredData,
    Parameters_StudentCaculation,
    Parameters_SystemCaculation,
    Parameters_DeviationCaculation,
    Parameters_SaturatedValue,
)
from app_R134aSimpleCyclePloting import systemCalculation
from PIL import Image
import base64
import io
import os
import json


# save the Json in a Json file
def saveDataFile(saveData):
    # define the name of the directory
    path = "./uuid/testUUID"

    # check whether directory already exists
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)

    # define the name of the directory with its subdirectories
    # path_sub = "./uuid/testUUID"
    # os.makedirs(path_sub)
    jsonDatasave = saveData.copy()
    jsonDatasave.pop("img_data")
    # feeds =[]
    # with open("./uuid/testUUID/savedata1.json", mode='w', encoding='utf-8') as f:
    #     json.dump([], f, indent = 6)
    # with open("./uuid/testUUID/savedata1.json", mode='w', encoding='utf-8') as feedsjson:
    #     feeds.append(jsonDatasave)
    #     json.dump(feeds, feedsjson, indent = 6)
    
    # 1. Read file contents
    with open("./uuid/testUUID/savedata1.json", "r",encoding='utf-8') as file:
        data = json.load(file)
    # 2. Update json object
    data.append(jsonDatasave)
    # 3. Write json file
    with open("./uuid/testUUID/savedata1.json", "w",encoding='utf-8') as file:
        json.dump(data, file,indent = 6)
    # save_file = open("./uuid/testUUID/savedata1.json", "w")  
    # json.dump(jsonDatasave, save_file, indent = 6)  
    # save_file.close()  

# save img in a json file
def saveImgFile(saveImg):
    # define the name of the directory
    path = "./uuid/testUUID"

    # check whether directory already exists
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)

    # define the name of the directory with its subdirectories
    # path_sub = "./uuid/testUUID"
    # os.makedirs(path_sub)
    jsonDatasave = saveImg.copy()
    jsonImgsave = jsonDatasave.pop("img_data")
    save_file = open("./uuid/testUUID/saveimg.json", "w")  
    json.dump(jsonImgsave, save_file, indent = 6)  
    save_file.close()


# get the img and encode it
def imgEncode():
    im = Image.open("server/uuid/test.png")
    data = io.BytesIO()
    im.save(data, "png")
    encoded_img_data = base64.b64encode(data.getvalue())
    # print(encoded_img_data.decode('utf-8'))

    return encoded_img_data.decode("utf-8")


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# sanity check route
@app.route("/enthapy", methods=["GET", "POST"])
def enthapy():
    response_object = {"status": "success"}
    if request.method == "POST":
        post_data = request.get_json()
        if post_data.get("dataType") == "Measured":
            Parameters_MeasuredData.update(
                {
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
                }
            )
            response_object["message"] = "Parameters_MeasuredData added!"
            print(response_object)
            if (
                Parameters_MeasuredData["MeasuredDataStatus"]
                == 1 & Parameters_StudentCaculation["CalculatedDataStatus"]
                == 1
            ):
                systemCalculation()
        elif post_data.get("dataType") == "Calculation":
            Parameters_StudentCaculation.update(
                {
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
                }
            )
            response_object["message"] = "Parameters_StudentCaculation added!"
            print(response_object)
            if (
                Parameters_MeasuredData["MeasuredDataStatus"]
                == 1 & Parameters_StudentCaculation["CalculatedDataStatus"]
                == 1
            ):
                systemCalculation()
                imgEncode()

        else:
            response_object["message"] = "Data hasn't been updated"
    # elif Response.status_code == 500:
    else:
        response_object["Parameters_MeasuredData"] = Parameters_MeasuredData
        response_object["Parameters_StudentCaculation"] = Parameters_StudentCaculation
        response_object["Parameters_SystemCaculation"] = Parameters_SystemCaculation
        response_object["Parameters_DeviationCaculation"] = (
            Parameters_DeviationCaculation
        )
        response_object["Parameters_SaturatedValue"] = Parameters_SaturatedValue
        response_object["img_data"] = imgEncode()

        saveDataFile(response_object)
        saveImgFile(response_object)
        # print(response_object)
        
    return jsonify(response_object)

    # return jsonify({
    #     'status': 'success',
    #     'parameters': Parameters,
    # })


# @app.errorhandler(500)
# def handle_server_error(error):
#     response_object = {"status": "fail"}
#     response_object["message"] = error
#     print(error)
#     return jsonify(response_object)


if __name__ == "__main__":
    app.run()

app.run(debug=True)
