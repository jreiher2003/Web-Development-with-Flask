import os
from flask import Flask, session, redirect, url_for, escape, request, make_response,Response
import datetime
import hashlib
import hmac 
import random
import bcrypt

SECRET = 'the_key'

app = Flask(__name__)

from functools import wraps
from flask import request, redirect, current_app

def ssl_required(fn):
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if current_app.config.get("SSL"):
            if request.is_secure:
                return fn(*args, **kwargs)
            else:
                return redirect(request.url.replace("http://", "https://"))
        
        return fn(*args, **kwargs)
            
    return decorated_view

####################################
############## bcrypt stuff ########
####################################
def super_pw_checker(password):
# password = b"super secret password"
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(12))
    print hashed

    if bcrypt.hashpw(password, hashed) == hashed:
        return "It matches"
    else:
        return "It no matches"

print super_pw_checker('finn7797')
####################################
####  hash passwords stuff  ########
####################################
def make_salt():
    n = 5
    return int(''.join(["%s" % random.randint(0,9) for num in range(0,n)]))


def make_pw_hash(name, pw, salt=None):
    """ return Hash(name + pw + salt), salt """
    if not salt:
        salt = str(make_salt())
    name = str(name)
    pw = str(pw)
    concat = hashlib.sha256(name+pw+salt).hexdigest()
    return concat, salt

# print make_pw_hash('jeff', 'finn')
def valid_pw(name, pw, h):
    """ returns true print valid_pw('name', 'pw', h) """
    salt = h[1]
    # print salt
    return h == make_pw_hash(name,pw,salt)

h = make_pw_hash('jeff', 'finn')
# print h
# print valid_pw('jeff', 'finn', h)
    
# x = 2 ** 256
# y = len(str(x))
# print x , y
# print "{:,}".format(x)



########################
####  cookie stuff  ####
########################
def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()


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

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
@ssl_required
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
@ssl_required
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