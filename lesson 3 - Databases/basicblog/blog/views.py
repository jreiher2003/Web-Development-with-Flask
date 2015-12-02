from flask import Flask, render_template, request, url_for, redirect
from blog import app 

@app.route('/')
def index():
	return render_template("base.html")