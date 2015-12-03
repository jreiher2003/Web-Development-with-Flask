from flask import render_template, request, redirect, url_for, flash
from blog import app, db
from models import *

@app.route('/')
def index():
	return 'hello'