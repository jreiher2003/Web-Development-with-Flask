import json
import urllib2

IP_URL = "http://ip-api.com/json/"
def get_coords(ip):
	url = IP_URL + ip
	content = None
	content = urllib2.urlopen(url).read()
	if content:
		result = json.loads(content)
		lon = result['lon']
		lat = result['lat']
		return lon, lat


print get_coords("4.2.2.2")