from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy.orm import sessionmaker
from datetime import date
from chan import app
from models import *





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