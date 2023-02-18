#pip install flask
#pip install flask-sqlalchemy

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hellow world"


@app.route("/about")
def about():
    return "About page"


if __name__== "__main__":
    app.run(debug=True)

#debug True = ошибки пишет которые будут. Если выставить False - то пользователю не будут видны оишбки