from app import app,db
from flask import render_template, g, url_for, request,redirect
from app.model import Entries

@app.route("/index",methods=["GET","POST"])
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/show_entries",methods=["GET","POST"])
def show_entries():
    entries = [elem.title for elem in Entries.query.all()]
    return render_template("show_entries.html",entries=entries)

@app.route("/add",methods=["POST"])
def add_entry():
    title = request.form.get("title")
    text = request.form.get("text")
    entry = Entries(title,text)
    db.session.add(entry)
    db.session.commit()
    return redirect(url_for("show_entries"))
