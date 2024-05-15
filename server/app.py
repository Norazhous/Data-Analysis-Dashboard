from flask import Flask, jsonify, request
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

Parameters = {
    # 'enthalpy':{
    # {
    #     'H1':1,
    # },
    # {
    #     'H2':2
    # }
    # },
    'MeasuredTime':0,
    'T1': 0,
    'T2': 0,
    'T3': 0,
    'T4': 0,
    'T5': 0,
    'P1': 0,
    'P2': 0,
    'P3': 0,
    'E':  0,
    'F':  0,
    'ASP':0,
    'H1':1,
    'H2':2,
    'COP':3,
}


# sanity check route
@app.route('/test', methods=['GET', 'POST'])
def test():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        Parameters.update({
            'MeasuredTime': post_data.get('MeasuredTime'),
            'T1': post_data.get('T1'),
            'T2': post_data.get('T2'),
            'T3': post_data.get('T3'),
            'T4': post_data.get('T4'),
            'T5': post_data.get('T5'),
            'P1': post_data.get('P1'),
            'P2': post_data.get('P2'),
            'P3': post_data.get('P3'),
            'E': post_data.get('E'),
            'F': post_data.get('F'),
            'ASP': post_data.get('ASP'),
        })
        response_object['message'] = 'Parameter added!'
    else:
        response_object['Parameters'] = Parameters
    return jsonify(response_object)

    # return jsonify({
    #     'status': 'success',
    #     'parameters': Parameters,
    # })


if __name__ == '__main__':
    app.run()

app.run(debug=True)