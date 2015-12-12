from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
md = Markdown(app)
db = SQLAlchemy(app)

from app import models, views
