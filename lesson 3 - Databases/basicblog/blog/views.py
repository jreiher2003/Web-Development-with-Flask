from flask import Flask, render_template, request, url_for, redirect
from blog import app 
from models import *

@app.route('/')
@app.route('/blog/')
def index():
	all_posts = db.GqlQuery('select * from Entry order by created desc')
	return render_template("front.html", all_posts=all_posts)

@app.route('/blog/newpost/', methods=['GET', 'POST'])
def newpost():
	if request.method == 'POST':
		subject = request.form['subject']
		blog = request.form['blog']
		newEntry = Entry(subject=subject, blog=blog)
		newEntry.put()

		return redirect(url_for('permalink'))

	if request.method == 'GET':
		return render_template('newpost.html')

@app.route('/blog/newEntry/')
def permalink():
	last_blog_post = db.GqlQuery('select * from Entry order by created asc limit 1')
	return render_template('permalink.html', last_blog_post=last_blog_post)