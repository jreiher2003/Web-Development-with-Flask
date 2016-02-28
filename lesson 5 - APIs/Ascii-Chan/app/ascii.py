import datetime
from ast import literal_eval
import urllib2
import json
from app import app, db
from app.models import AsciiArt
from flask import render_template, request, url_for, redirect


IP_URL = "http://ip-api.com/json/"
def get_coords(ip):
	ip = "4.2.2.2"
	url = IP_URL + ip
	content = None
	content = urllib2.urlopen(url).read()
	if content:
		result = json.loads(content)
		lon = float(result['lon'])
		lat = float(result['lat'])
		return lat,lon


def gmaps_img(points):
    GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=580x300&zoom=3&sensor=false"
    for lat, lon in points:
        GMAPS_URL += '&markers=%s,%s' % (lat, lon)
    return GMAPS_URL


@app.route("/", methods=["GET","POST"])
def hello():
    all_art = AsciiArt.query.order_by(AsciiArt.id.desc()).all()
    all_art = list(all_art)
    lat = []
    lon = []
    for a in all_art:
        lat.append(a.lat)
    for b in all_art:
        lon.append(b.lon)
    x = zip(lat,lon)
    img_url = None
    img_url = gmaps_img(x)
    if request.method == 'POST':
        one = AsciiArt(title=request.form['title'], art=request.form['art'])
        lat = get_coords(request.remote_addr)[0]
        lon = get_coords(request.remote_addr)[1]
        if lat and lon:
            one.lat = lat
            one.lon = lon
        db.session.add(one)
        db.session.commit()
        return redirect(url_for('hello', all_art=all_art, img_url=img_url))
    return render_template("base.html", all_art=all_art, img_url=img_url)

