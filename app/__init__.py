from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

app = Flask(__name__)
md = Markdown(app)

from app import models, views
