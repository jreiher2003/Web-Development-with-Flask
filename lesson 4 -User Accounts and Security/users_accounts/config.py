import os


# default config
class BaseConfig(object):
    """ common configs between local and production """
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = '\xa8p\xa2\xf1\xf2j\xeb\xd3j\xaa\x8c\xc8\x87L0'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'