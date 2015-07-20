"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, url_for, redirect, request, flash
from utils import valid_username, valid_password, valid_email
import re
app = Flask(__name__)
app.secret_key = 'super_secret_key'
app.config['DEBUG'] = True
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/rot13', methods=["GET","POST"])
def rot13():
	if request.method == "GET":
		return render_template('rot13.html')
	if request.method == 'POST':
		rot = request.form['text']
		if rot:
			rots = rot.encode('rot13')
			return render_template('rot13.html', rots=rots)
	
@app.route('/signup', methods=["GET", "POST"])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')

	if request.method == 'POST':
		username = valid_username(request.form['username'])
		password = valid_password(request.form['password'])
		vpw = valid_password(request.form['vpw'])
		email = valid_email(request.form['email'])

		if not (username and password and vpw):
			if username is None or password is None or vpw is None:
				username = request.form['username']
				password = request.form['password']
				vpw = request.form['vpw']
			

			flash('You have an error you need to fix son')
			
			return render_template('signup.html', username=username, password=password, vpw=vpw)
		return redirect(url_for('welcome',username=username))

@app.route('/welcome/<username>')
def welcome(username):

	return render_template('welcome.html', username=username)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500