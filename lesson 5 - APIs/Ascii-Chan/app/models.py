import datetime
from app import db

class AsciiArt(db.Model):
	__tablename__ = 'asciiart'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	art = db.Column(db.String)
	created = db.Column(db.Date, default=datetime.datetime.now())

	def __init__(self, title, art):
		self.title = title
		self.art = art

	@property 
	def format_date(self):
		return '{dt:%A} {dt:%B} {dt.day}, {dt.year}'.format(dt=self.adopt_date)

	def __repr__(self):
		return '<title>: {}'.format(self.title)