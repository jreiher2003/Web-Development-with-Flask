from flask import render_template, request, redirect, url_for, flash
from blog import app, db
from models import *

@app.route('/')
@app.route('/blog/')
def index():
	all_posts = db.session.query(Entry).all()
	return render_template('front.html', all_posts=all_posts)

@app.route('/blog/newpost/', methods=['GET', 'POST'])
def newpost():
	if request.method == 'POST':
		subject = request.form['subject']
		blog = request.form['blog']
		newEntry = Entry(subject=subject, blog=blog)
		db.session.add(newEntry)
		db.session.commit()
		last_id = db.session.query(Entry).order_by(Entry.id.desc()).first()
		return redirect(url_for('permalink', id=last_id.id))

	if request.method == 'GET':
		return render_template('newpost.html')

@app.route('/blog/<id>/')
def permalink(id):
	last_entry = db.session.query(Entry).order_by(Entry.id.desc()).first()
	return render_template('permalink.html', last_entry=last_entry)