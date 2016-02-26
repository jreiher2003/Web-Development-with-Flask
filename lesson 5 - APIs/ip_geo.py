import json
import urllib2

IP_URL = "http://ip-api.com/json/"
def get_coords(ip):
	url = IP_URL + ip
	content = None
	content = urllib2.urlopen(url).read()
	if content:
		result = json.loads(content)
		# print result.keys()
		return result['lon']


print get_coords("73.55.103.114")