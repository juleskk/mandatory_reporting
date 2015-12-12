from app import app
from flask import render_template, g, url_for, request

@app.route("/index",methods=["GET","POST"])
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

