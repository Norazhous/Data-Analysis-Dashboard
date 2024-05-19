from flask import Flask, jsonify, request, Response,render_template
from flask_cors import CORS
from app_globalVal import (
    Parameters_MeasuredData,
    Parameters_StudentCaculation,
    Parameters_SystemCaculation,
    Parameters_DeviationCaculation,
    Parameters_SaturatedValue,
)
from app_R134aSimpleCyclePloting import systemCalculation


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# sanity check route
@app.route("/test", methods=["GET", "POST"])
def test():
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
        else:
            response_object["message"] = "Data hasn't been updated"
    # elif Response.status_code == 500:
    else:
        response_object["Parameters_MeasuredData"] = Parameters_MeasuredData
        response_object["Parameters_StudentCaculation"] = Parameters_StudentCaculation
        response_object["Parameters_SystemCaculation"] = Parameters_SystemCaculation
        response_object["Parameters_DeviationCaculation"] = Parameters_DeviationCaculation
        response_object["Parameters_SaturatedValue"] = Parameters_SaturatedValue   
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
