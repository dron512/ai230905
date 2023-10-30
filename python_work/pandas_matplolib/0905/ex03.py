from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/aa")
def aa():
    return "aa"

@app.route("/a")
def a():
    a = 10+20
    return render_template("a.html",a=a)

app.run(debug=True)