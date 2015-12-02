from flask import Flask 
from blog import app 

@app.route('/')
def index():
	return "Basic Blog start"