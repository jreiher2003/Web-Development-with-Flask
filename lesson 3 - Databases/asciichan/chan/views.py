from flask import Flask, render_template, request, redirect, url_for, flash

from datetime import date
from chan import app
from models import *



@app.route('/', methods=['GET', 'POST'])
def hello_world():
	all_art = db.GqlQuery("select * from Art order by created desc")

	if request.method == 'POST':
		title = request.form['title']
		art = request.form['art']
		if title and art:
			newArt = Art(title=title, art=art)
			newArt.put()
			flash('Thanks for submitting!', 'success')
			return redirect(url_for('hello_world'))
		else:
			flash('You need both title and artwork', 'danger')
			return redirect(url_for('hello_world'))
		
		

	if request.method == 'GET':
		return render_template('front.html', all_art=all_art)