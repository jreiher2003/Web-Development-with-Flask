from config import SQLALCHEMY_DATABASE_URI
from blog import db

db.create_all()