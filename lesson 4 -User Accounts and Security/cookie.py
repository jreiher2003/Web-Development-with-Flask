import os
from flask import Flask, session, redirect, url_for, escape, request, make_response,Response
import datetime
app = Flask(__name__)


# sessions
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

# remove the username from the session if it's there
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


# set the secret key.  keep this really secret:
@app.route('/counting/')
def count_me():
    visits = request.cookies.get('visits', 0)
    try:
        visits
        if visits.isdigit():
            visits = int(visits) + 1
    except AttributeError:
        visits = 0
    response = make_response("you have been here %s times!" % visits)
    response.set_cookie('visits', value='%s' % visits)
    if visits > 100000:
        return make_response("You are awesome")
    else:
        return response


#reading cookies
@app.route('/count/')
def count_clicks():
    response = make_response('you are responing')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.set_cookie('JeffsCookie',value='jeff', max_age=50000, expires=datetime.datetime.now() + datetime.timedelta(days=30))
    return response


# set cookie
@app.route('/set_cookie')
def cookie_insertion():
    try:
        session['visits'] +=1
    except KeyError:
        session['visits'] = 0
    response = make_response('redirect_me %s' % session['visits'])
    response.set_cookie('visits',value=str(session['visits']))
    return response


@app.route('/new')
def count_a_cookie():
    try:
        session['visits'] +=1
    except KeyError:
        session['visits'] = 0
    return 'Visits: %s' % session['visits']


@app.route('/jeff')
def cookie_count():
    try:
        session['visits'] +=1
    except KeyError:
        session['visits'] = 0

    response = make_response("Visits: %s" % session['visits'])
    response.set_cookie('visits', value=str(session['visits']), expires=datetime.datetime.now() + datetime.timedelta(days=30))
    return response


@app.route('/clear')
def clearsession():
    session.clear()
    response = make_response(redirect(url_for('count_me')))
    response.set_cookie('visits', value='0')
    return response


if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)