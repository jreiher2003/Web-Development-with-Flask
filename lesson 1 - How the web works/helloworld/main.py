from flask import Flask, render_template, make_response, request, redirect, url_for
from utils import valid_month, valid_day, valid_month

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
form = """
<form action="/testform" method="POST">
	<input name="q">
	<input type="submit">
</form>
"""
# birthday validation
form2 = """
<form action="/birthday" method="POST">
	What is your birthday?
	<br>
	<label>Month
	<input type="text" name="month">
	</label>
	<label>Day
	<input type="text" name="day">
	</label>
	<label>Year
	<input type="text" name="year">
	</label>
	<br>
	<br>
	<input type="submit">
</form>
"""

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    response = make_response(form)
    # response.headers['Content-Type'] = 'text/html'
    return response

@app.route('/lesson2')
def lesson2():
	return render_template('play.html')

@app.route('/testform', methods=['GET', 'POST'])
def TestHandler():
	if request.method == 'POST':
		name = request.form['q']
		response = make_response(name)
		return response
	else:
		return url_for('hello')

# birthday validation
@app.route('/birthday', methods=['GET','POST'])
def birthday():
	if request.method == "GET":
		response = make_response(form2)
		return response 

	if request.method == 'POST':
		user_month = request.form['month']
		user_day = request.form['day']
		user_year = request.form['year']

		if not (user_month and user_day and user_year): # don't forget () won't work without it
			response = make_response(form2)
			return response
		else:
			return "Thanks that is a totally valid day"
		



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404