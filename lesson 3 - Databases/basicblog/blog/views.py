from flask import Flask, render_template, request, url_for, redirect
from blog import app 

@app.route('/')
@app.route('/blog/')
def index():
	return render_template("base.html")

@app.route('/blog/newpost/', methods=['GET', 'POST'])
def newpost():
	if request.method == 'POST':
		subject = request.form['subject']
		blog = request.form['blog']
		return render_template('base.html')

	if request.method == 'GET':
		return render_template('newpost.html')