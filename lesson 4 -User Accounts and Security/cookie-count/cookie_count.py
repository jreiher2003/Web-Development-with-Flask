# We'll need the session object to manage session variables
# render_template to render html content from templates
# url_for to extract the url for a given view/route
# request to access the GET data request for the form view
# redirect to perform redirects to different routes
from flask import Flask, session, render_template, url_for, request, redirect

app = Flask(__name__)

# Sessions variables are stored client side, on the users browser
# the content of the variables is encrypted, so users can't
# actually see it. They could edit it, but again, as the content
# wouldn't be signed with this hash key, it wouldn't be valid
# You need to set a scret key (random text) and keep it secret
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

# We'll use this function later to initialise or increment
# a counter that will be stored as a session variable
# This function will be called from every route, so it will
# keep a record of how many routes/pages have been loaded
def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

# Define a route for the main page
# The index template will be loaded, showing a counter and also
# a session variable containing the user's name, if it has been set
# or a link to set it otherwise
@app.route('/')
def index():
    # Initialise the counter, or increment it
    sumSessionCounter()
    return render_template('index.html')

# Form route - Will show a form where the user can set its name
# and will be set as a session variable
@app.route('/form')
def form():
  sumSessionCounter()
  # if a name has been sent, store it on a session variable
  if request.args.get('yourname'):
    session['name'] = request.args.get('yourname')
    # And then redirect the user to the main page
    return redirect(url_for('index'))
  else:
    # If no name has been sent, show the form
    return render_template('form.html', session=session)

# This dummy page will just load the session data
@app.route('/page1')
def page1():
  session['counter'] = session['counter'] + 1
  # if is sset name, store it on session
  return render_template('page1.html')

# This dummy page will just load the session data
@app.route('/page2')
def page2():
  session['counter'] = session['counter'] + 1
  # if is sset name, store it on session
  return render_template('page2.html')

# This route will clear the variable sessions
# This functionality can come handy for example when we logout
# a user from our app and we want to clear its information
@app.route('/clear')
def clearsession():
    # Clear the session
    session.clear()
    # Redirect the user to the main page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)