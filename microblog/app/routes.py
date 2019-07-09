from app import app
from flask import render_template


@app.route("/")
@app.route('/index')
def index():
    user = {"username": "ride"}
    return render_template("index.html", title="home", user=user)
