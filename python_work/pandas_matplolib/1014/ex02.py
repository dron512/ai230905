from flask import Flask, request, jsonify, Response, render_template
from flask_cors import CORS
import kn
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def index():
    param = request.get_json()
    len = int(param['len'])
    wei = int(param['wei'])
    pred = str(kn.kn.predict([[len, wei]]))
    return jsonify({"msg": pred})

@app.route("/aa", methods=['POST'])
def aa():
    return render_template('aa.html')


@app.route("/img1/<int:x>/img1/<int:y>")
def img1(x,y):
    print(x)
    print(y)
    plt.figure(figsize=(8, 6))
    plt.scatter(kn.bream_length, kn.bream_weight)
    plt.scatter(kn.smelt_length, kn.smelt_weight)
    plt.scatter(kn.my_length, kn.my_weight)
    plt.scatter(x,y,s=500)

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return Response(img_buffer, content_type='image/png')


app.run(debug=True, host="0.0.0.0")
