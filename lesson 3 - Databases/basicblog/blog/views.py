from flask import Flask, render_template, request, url_for, redirect, flash
from blog import app 
from models import *

@app.route('/')
@app.route('/blog/')
def index():
	all_posts = db.GqlQuery('select * from Entry order by created desc limit 10')
	return render_template("front.html", all_posts=all_posts)

@app.route('/blog/newpost/', methods=['GET', 'POST'])
def newpost():
	if request.method == 'POST':
		subject = request.form['subject']
		blog = request.form['blog']
		if subject and blog:
			newEntry = Entry(parent= blog_key(), subject=subject, blog=blog)
			newEntry.put()
			flash('Thanks for your submission!', 'danger')
			return redirect(url_for('permalink', post_id=newEntry.key().id()))
		else:
			flash('You need both subject and blog entry', 'danger')
			return render_template('newpost.html')


	if request.method == 'GET':
		return render_template('newpost.html')

@app.route('/blog/<post_id>/')
def permalink(post_id):
    key = db.Key.from_path('Entry', int(post_id), parent=blog_key())
    post = db.get(key)
    if not post:
        self.error(404)
        return
    return render_template('permalink.html', post=post)