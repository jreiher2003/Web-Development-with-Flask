from app import app, db
from flask import flash, redirect, render_template, request, url_for
from flask.ext.login import login_user, logout_user, login_required
from forms import LoginForm, RegisterForm
from app.models import User, bcrypt

@app.route('/')
def index():
	return render_template('home.html')


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
@login_required
def logout():
	logout_user()
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