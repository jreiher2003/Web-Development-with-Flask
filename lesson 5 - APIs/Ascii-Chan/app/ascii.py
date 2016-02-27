import datetime
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
		lon = result['lon']
		lat = result['lat']
		return (lat, lon)
	

GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=580x300&zoom=13&sensor=false&markers=26.876,-82.2681"
def gmaps_img():
    # markers = '&'.join('markers=%s,%s' % (p.lat, p.lon) for p in points)
    # return GMAPS_URL+markers
    return GMAPS_URL

@app.route("/", methods=["GET","POST"])
def hello():
    points = get_coords(request.remote_addr)
    img_url = gmaps_img()
    
    all_art = AsciiArt.query.order_by(AsciiArt.id.desc()).all()
    arts = list(all_art)
    # points = filter(None, (a.coords for a in arts))
    img_url = None
    img_url = gmaps_img()

    if request.method == 'POST':
        coords1 = get_coords(request.remote_addr)
        one = AsciiArt(title=request.form['title'], art=request.form['art'], coords=str(coords1))
        # if coords1:
        #     one.coords = coords1
    	
        db.session.add(one)
        db.session.commit()
        return redirect(url_for('hello', all_art=all_art, img_url=img_url, points=points))
    return render_template("base.html", all_art=all_art, img_url=img_url, points=points)

