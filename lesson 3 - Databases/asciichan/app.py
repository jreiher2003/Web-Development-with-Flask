from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

app = Flask(__name__)

Base = declarative_base()	


class Art(Base):
	__tablename__ = 'art'
	id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
	title = Column(String(250), nullable=False)
	art = Column(String, nullable=False)
	created = Column(Date)

engine = create_engine('sqlite:///artwork.db' , echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	all_art = session.query(Art).order_by(desc('art.created'))
	if request.method == 'GET':
		return render_template('front.html', all_art=all_art)

	if request.method == 'POST':
		title = request.form['title']
		art = request.form['art']
		created = date.today()
		if title and art and created:
			error = 'need a title and art'
			success ="Thanks for submitting"
			newArt = Art(title=title, art=art, created=created)
			session.add(newArt)
			session.commit()
			return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run(debug=True)
