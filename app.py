from flask import Flask, render_template, redirect, jsonify, url_for, request
from flask_cors import CORS, cross_origin
from brains import serve
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    print("Server Starting....")
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_request():
    try:
        print("Processing Request....")
        graph_dict = json.loads(request.get_json()['structure'])
        result_dict = serve(graph_dict)
        print(f'RESULTS#######\n\n{result_dict}\n\n')
        res_obj = result_dict

        """ # UNCOMMENT IF U WANT TO TEST WITH THE structure.json file OR IF U WANT TO USE THE IPYNB FILE TO TEST ######
        f = open('./static/json/structure.json', mode='w+')
        f.write(json.dumps(graph_dict))
        f.close()
        f = open('.static/json/processed_structure.json', mode='w+')
        f.write(json.dumps(result_dict))
        f.close() """

        return jsonify(res_obj), 201, {'Content-Type': 'application/json'}
    except:
        return "400 Bad request error"


@app.errorhandler(400)
def handle_bad_request(e):
    return 'bad request!', 400

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)

