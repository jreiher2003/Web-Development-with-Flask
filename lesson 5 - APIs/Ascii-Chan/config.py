

class ConfigClass(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_DATABASE_URI = "sqlite:///ascii.db"
	SECRET_KEY = "the-secret-is-here"