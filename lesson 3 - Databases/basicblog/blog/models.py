from blog import db

class Entry(db.Model):
    __tablename__ = 'entry' # names table
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80), nullable=False)
    blog = db.Column(db.String, nullable=False)
    created = db.Column(db.Date)

