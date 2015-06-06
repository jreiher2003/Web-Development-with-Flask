from flask import Flask, render_template, make_response, request, redirect, url_for, flash
from utils import valid_month, valid_day, valid_year

app = Flask(__name__)
app.secret_key = 'super_secret_key'
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
form = """
<form action="/testform" method="POST">
	<input name="q">
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

@app.route('/confirm')
def confirm():
	return render_template('confirm.html')

# birthday validation
@app.route('/birthday', methods=['GET','POST'])
def birthday():
	if request.method == "GET":
		return render_template('birthday.html') 

	if request.method == 'POST':
		# functions on data in form
		user_month = valid_month(request.form['month'])
		user_day = valid_day(request.form['day'])
		user_year = valid_year(request.form['year'])
		

		if not (user_month and user_day and user_year): # don't forget () won't work without it
			if user_month is None or user_day is None or user_year is None:
				user_month = request.form['month'] 
				user_day = request.form['day']
				user_year = request.form['year']
			flash('error you did not provide a valid date')
			return render_template('birthday.html', month=user_month, day=user_day, year=user_year)
		return redirect(url_for('confirm'))	
	



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404