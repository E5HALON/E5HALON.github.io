from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mile", methods=["POST"])
def mile():
    return render_template("mile.html", name=request.form.get("name", "World"))

