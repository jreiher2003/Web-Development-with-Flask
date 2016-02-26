from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.ConfigClass')
db = SQLAlchemy(app)

from app import ascii, models
from models import * 