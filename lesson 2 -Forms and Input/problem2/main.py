"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)
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
	

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500