import datetime
import urllib2
import json
from app import app, db
from app.models import AsciiArt
from flask import render_template, request, url_for, redirect

IP_URL = "http://ip-api.com/json/"
def get_coords(ip):
	url = IP_URL + ip
	content = None
	content = urllib2.urlopen(url).read()
	if content:
		result = json.loads(content)
		# print result.keys()
		lon = result['lon']
		lat = result['lat']
		return lat, lon
	else:
		return None

@app.route("/", methods=["GET","POST"])
def hello():
    all_art = AsciiArt.query.all()
    if request.method == 'POST':
        one = AsciiArt(title=request.form['title'], art=request.form['art'])
        db.session.add(one)
        db.session.commit()
        return redirect(url_for('hello', all_art=all_art))
    return render_template("base.html", all_art=all_art)

