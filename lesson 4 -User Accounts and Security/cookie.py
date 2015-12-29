import os
from flask import Flask, session, redirect, url_for, escape, request, make_response,Response
import datetime
import hashlib

app = Flask(__name__)

def hash_str(s):
    return hashlib.md5(s).hexdigest()


def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))
# print make_secure_val('1')

def check_secure_val(h):
    # h = str(h)
    val = h.split('|')[0].strip()
    hash_val = h.split('|')[1].strip()
    # print hash_val
    check_val =  make_secure_val(val).split('|')[1].strip()
    # print check_val
    if hash_val == check_val:
        return val
    else:
        return None
# print check_secure_val('1|c4ca4238a0b923820dcc509a6f75849b')
# set the secret key.  keep this really secret:
@app.route('/counting/')
def count_me():
    visits = request.cookies.get('visits',0)
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
    return response

@app.route('/check')
def check_me():
    visits = 0
    visit_cookie_str = request.cookies.get('visits')
    if visit_cookie_str:
        cookie_val = check_secure_val(visit_cookie_str)
        if cookie_val:
            visits = int(cookie_val)
    visits +=1
    new_cookie_val = make_secure_val(str(visits))
    response = make_response("You have been here %s" % visits)
    response.set_cookie("visits", value='%s' % new_cookie_val)
    return response

# sessions
@app.route('/')
@app.route('/clear')
def clearsession():
    session.clear()
    response = make_response(redirect(url_for('count_me')))
    response.set_cookie('visits', value='0')
    return response


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
    has = make_secure_val(str(session['visits']))
    if check_secure_val(has) != None:
        response.set_cookie('visits',value=has)
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




if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)