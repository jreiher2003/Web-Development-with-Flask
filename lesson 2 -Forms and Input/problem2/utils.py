import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
	username = USER_RE.match(username)
	if username:
		return username.group(0)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
	password = PASS_RE.match(password)
	if password:
		return password.group(0)

EMAIL_RE = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
def valid_email(email):
	email = EMAIL_RE.match(email)
	if email:
		return email.group(0)