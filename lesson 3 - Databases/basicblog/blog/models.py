from google.appengine.ext import db


def blog_key(name = 'default'):
	return db.Key.from_path('blogs', name)
	
class Entry(db.Model):
	subject = db.StringProperty(required=True)
	blog = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)
	last_modified = db.DateTimeProperty(auto_now = True)