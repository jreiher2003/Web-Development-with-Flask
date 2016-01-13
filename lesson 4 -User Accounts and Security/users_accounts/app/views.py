from app import app, db
from flask import flash, redirect, render_template, request, url_for, session, make_response
from flask.ext.login import login_user, logout_user, login_required, current_user
from forms import LoginForm, RegisterForm, MessageForm
from app.models import User, BlogPost, bcrypt
import hmac 


def hash_str(s):
    return hmac.new(app.config['SECRET_KEY'], s).hexdigest()


def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('|')[0].strip()
    hash_val = h.split('|')[1].strip()
    check_val =  make_secure_val(val).split('|')[1].strip()
    if hash_val == check_val:
        return val
    else:
        return None


# @app.route('/')
# def onlyCookie():
#     response = make_response(redirect(url_for('onlyCookie')))
#     response.set_cookie('visits', value='0')
#     visits = request.cookies.get('visits',0)
#     try:
#         visits
#         visits = visits.split('|')[0]
#         if visits.isdigit():
#             visits = int(visits) + 1
#     except AttributeError:
#          visits = 0
#     has = make_secure_val(str(visits))
#     if check_secure_val(has) != None:
#         if visits < 100:
#             response = make_response("you have been here %s times!" % visits)
#             response.set_cookie('visits', value='%s' % has)
#         else:
# 			response = make_response("Your awesome")
# 			response.set_cookie('visits', value='%s' % has)
#     elif check_secure_val(has) == None:
#         visits = 0
#     	response = make_response("cookie value doesn't make the hash now the value is %s" % visits)
#     	response.set_cookie('visits', value=0)
    
#     return response


@app.route('/', methods=['GET', 'POST'])
# @login_required
def index():
	error = None
	form = MessageForm(request.form)
	if request.method == 'POST':
	    if form.validate_on_submit():
			new_post = BlogPost(form.title.data,form.description.data,current_user.id)
			db.session.add(new_post)
			db.session.commit()
			flash('New Post was successfully posted.', 'bg-success')
			return redirect(url_for('index'))
	else:
		posts = db.session.query(BlogPost).all()
		return render_template('home.html', posts=posts,form=form, error=error)


@app.route('/login', methods=["GET", "POST"])
def login():
	error = None
	form = LoginForm(request.form)
	if request.method == "POST":
		if form.validate_on_submit():
			user = User.query.filter_by(name=request.form['username']).first()
			if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
				login_user(user)
				flash("You were logged in. Go Crazy.", 'bg-success')
				return redirect(url_for('index'))
			else:
				flash("Try again", "bg-danger")
				return redirect(url_for('login'))
	return render_template("login.html", form=form, error=error)




@app.route('/logout')
# @login_required
def logout():
    # logout_user()
    session.clear()
    response = make_response(redirect(url_for('index')))
    response.set_cookie('visits', value='0')
    flash('You were logged out.', 'bg-danger')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(name=form.username.data,
					email=form.email.data,
					password=form.password.data)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect(url_for('index'))
	return render_template('register.html', form=form)