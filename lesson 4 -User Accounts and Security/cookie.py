from flask import Flask, session, redirect, url_for, escape, request, make_response

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

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:

#reading cookies
@app.route('/count/')
def count_clicks():
    visits = request.cookies.get('visits', 0)
    session['visits'] += 1
    resp = make_response("You have been here %s times!" % visits)
    resp.set_cookie('visits', '%s' % visits)
    return resp

# storing cookie
@app.route('/2')
def index2():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('username', 'Jeff Reiher')
    return resp

# set cookie
@app.route('/set_cookie')
def cookie_insertion():
    redirect_to_index = redirect('/index')
    response = current_app.make_response(redirect_to_index )  
    response.set_cookie('cookie_name',value='values')
    return response


if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    # app.debug = True
    app.run(debug=True)