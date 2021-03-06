from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.bcrypt import Bcrypt 
from flask.ext.login import LoginManager 
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)

import views
from models import User 

login_manager.login_view = "login" 
login_manager.login_message = u'You need to login first' 
# login_manager.login_category = 'info' 

# loads users info from db and stores it in a session
@login_manager.user_loader 
def load_user(user_id):
	return User.query.filter(User.id == int(user_id)).first()