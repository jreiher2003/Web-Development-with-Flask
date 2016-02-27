import datetime
from app import db

class AsciiArt(db.Model):
	__tablename__ = 'asciiart'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	art = db.Column(db.String)
	created = db.Column(db.Date, default=datetime.datetime.now())
	coords = db.Column(db.String)

	def __init__(self, title, art, coords):
		self.title = title
		self.art = art
		self.coords = coords
		

	@property 
	def format_date(self):
		return '{dt:%A} {dt:%B} {dt.day}, {dt.year}'.format(dt=self.created)

	def __repr__(self):
		return '<title>: {}'.format(self.title)