from flask import Flask
from action import random_num, hello_user
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/step1")
def step1():
    return random_num()


@app.route("/step2", methods=["GET", "POST"])
def step2():
    if "login" in request.form.keys():
        values = request.values
        print(values)
        return str({"login": values["login"], "psw": values["psw"]})


@app.route("/step3", methods=["GET", "POST"])
def step3():
    if "login" in request.form.keys():
        values = request.values
        return hello_user(values["login"])


app.run(debug=True)
