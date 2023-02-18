#pip install flask
#pip install flask-sqlalchemy

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/user/<string:name>/<int>:id")
def user(name, id):
    return "User page: " + name + "  -  " + str(id)


if __name__== "__main__":
    app.run(debug=True)

#debug True = ошибки пишет которые будут. Если выставить False - то пользователю не будут видны оишбки