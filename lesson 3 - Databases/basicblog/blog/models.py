from google.appengine.ext import db


class Entry(db.Model):
	subject = db.StringProperty(required=True)
	blog = db.StringProperty(required=True)
	created = db.DateProperty(auto_now_add=True)