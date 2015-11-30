from flask import Flask, render_template, request, redirect, url_for, flash
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

	if request.method == 'POST':
		title = request.form['title']
		art = request.form['art']
		created = date.today()
		if title and art:
			newArt = Art(title=title, art=art, created=created)
			session.add(newArt)
			session.commit()
			flash('Thanks for submitting!', 'success')
			return redirect(url_for('hello_world'))
		else:
			flash('You need both title and artwork', 'danger')
			return redirect(url_for('hello_world'))
		
		

	if request.method == 'GET':
		return render_template('front.html', all_art=all_art)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host="localhost", port=5000)
