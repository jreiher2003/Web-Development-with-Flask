import os
from flask import Flask, session, redirect, url_for, escape, request, make_response,Response
import datetime
app = Flask(__name__)


def write(self, *a, **kw):
    return self.response.out.write(*a, **kw)
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

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


# set the secret key.  keep this really secret:
@app.route('/counting/')
def count_me():
    # response.headers['Content-Type'] = 'text/plain'
    visits = request.cookies.get('visits', 0)
    visits =+1
    return "you have been here %s times!" % visits


#reading cookies
@app.route('/count/')
def count_clicks():
    response = make_response('you are responing')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.set_cookie('JeffsCookie',value='jeff', max_age=50000, expires=datetime.datetime.now() + datetime.timedelta(days=30))
   
    return response
     

@app.route('/redirect-link')
def redirect_me():
    visits = request.cookies.get('visits')
    # int(visits) = visits
    response = make_response("You just go redirected to here %s times!" % visits)
    return response
# set cookie
@app.route('/set_cookie')
def cookie_insertion():
    # redirect_to_index = redirect(url_for('cookie_insertion'))
    session['visits'] += 1
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
    return redirect(url_for('count_a_cookie'))

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    # app.debug = True
    
    app.run(debug=True)