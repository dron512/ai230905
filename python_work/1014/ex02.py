from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/", methods=['POST'])
def index():
    param = request.get_json()
    print(param)
    return jsonify({"msg":"success"})

app.run(debug=True,host="0.0.0.0")