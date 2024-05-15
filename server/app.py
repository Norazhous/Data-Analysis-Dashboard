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
            'H3': post_data.get('H3'),
            'H4': post_data.get('H4'),
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