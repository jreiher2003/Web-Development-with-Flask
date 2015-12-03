from google.appengine.ext import db


class Entry(db.Model):
	subject = db.StringProperty(required=True)
	blog = db.TextProperty(required=True)
	created = db.DateProperty(auto_now_add=True)
	last_modified = db.DateTimeProperty(auto_now = True)