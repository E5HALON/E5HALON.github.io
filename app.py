from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Sign-in", method=["POST"])
def signin():
    return render_template("Sign-in.html", name=request.form.get("name", "World"))


@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/User Profile", method=["POST"])
def userprofile():
    return render_template("User Profile.html", name=request.form.get("E-mail"))