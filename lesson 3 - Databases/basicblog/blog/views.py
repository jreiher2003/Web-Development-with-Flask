from flask import Flask, render_template, request, url_for, redirect
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
		newEntry = Entry(subject=subject, blog=blog)
		newEntry.put()
		# key = db.Key.from_path('subject', subject, 'blog', blog )
		# post = db.get(key)
		return redirect(url_for('index'))

	if request.method == 'GET':
		return render_template('newpost.html')

@app.route('/blog/<int:blog_id>/')
def permalink(blog_id):
	# key = db.Key.from_path('Entry', blog_id)
	# post = db.get(key)
	last_blog_post = db.GqlQuery('select * from Entry order by created asc limit 1')
	blog_id = last_blog_post.key().id_or_name()
	return render_template('permalink.html', blog_id=blog_id)