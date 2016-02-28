import datetime
from ast import literal_eval
import urllib2
import json
from app import app, db
from app.models import AsciiArt
from app.forms import AsciiForm
from flask import render_template, request, url_for, redirect, flash


IP_URL = "http://ip-api.com/json/"
def get_coords(ip):
    ip = "4.2.2.2"
    ip = "23.24.209.141"
    url = IP_URL + ip
    content = None
    content = urllib2.urlopen(url).read()
    if content:
        result = json.loads(content)
        lon = float(result['lon'])
        lat = float(result['lat'])
        return lat,lon


def gmaps_img(points):
    GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=550x400&zoom=3&sensor=false"
    for lat, lon in points:
        GMAPS_URL += '&markers=%s,%s' % (lat, lon)
    return GMAPS_URL


@app.route("/", methods=["GET","POST"])
def hello():
    error = None
    form = AsciiForm()
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
    if form.validate_on_submit():
        one = AsciiArt(title=form.title.data, art=request.form['art'])
        lat = get_coords(request.remote_addr)[0]
        lon = get_coords(request.remote_addr)[1]
        if lat and lon:
            one.lat = lat
            one.lon = lon
        db.session.add(one)
        db.session.commit()
        flash("You just posted some <strong>ascii</strong> artwork!", 'success')
        return redirect(url_for('hello'))
    return render_template("base.html", all_art=all_art, img_url=img_url, form=form, error=error)

