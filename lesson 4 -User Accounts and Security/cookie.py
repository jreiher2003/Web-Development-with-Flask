import os
from flask import Flask, session, redirect, url_for, escape, request, make_response,Response
import datetime
import hashlib
import hmac 

SECRET = 'the_key'

app = Flask(__name__)

print hashlib.md5("110").hexdigest()

def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()
# print has_str1('yo')

# def hash_str(s):
#     return hashlib.md5(s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))
# print make_secure_val('1')

def check_secure_val(h):
    val = h.split('|')[0].strip()
    hash_val = h.split('|')[1].strip()
    check_val =  make_secure_val(val).split('|')[1].strip()
    if hash_val == check_val:
        return val
    else:
        return None


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
        response.set_cookie('visits',value=has, path='/set_cookie', expires=datetime.datetime.now() + datetime.timedelta(days=30))
    return response

# set cookkie without a session cookie
@app.route('/only_cookie')
def onlyCookie():
    visits = request.cookies.get('visits',0)
    try:
        visits
        visits = visits.split('|')[0]
        if visits.isdigit():
            visits = int(visits) + 1
    except AttributeError:
         visits = 0
    has = make_secure_val(str(visits))
    if check_secure_val(has) != None:
        if visits < 100:
            response = make_response("you have been here %s times!" % visits)
            response.set_cookie('visits', value='%s' % has)
        else:
			response = make_response("Your awesome")
			response.set_cookie('visits', value='%s' % has)
    elif check_secure_val(has) == None:
        visits = 0
    	response = make_response("cookie value doesn't make the hash now the value is %s" % visits)
    	response.set_cookie('visits', value=0)
    
    return response
    
    
    
@app.route('/')
@app.route('/clear')
def clearsession():
    session.clear()
    response = make_response(redirect(url_for('onlyCookie')))
    response.set_cookie('visits', value='0')
    return response



if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)