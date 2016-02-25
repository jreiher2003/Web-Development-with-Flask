import json 
import urllib2 
from pprint import pprint 


def parse_reddit_json():
	hdr = { "User-Agent" : "Jeff Reiher practicing python scripts with json"}
	req = urllib2.Request("https://www.reddit.com/.json", headers=hdr)
	p = urllib2.urlopen(req).read()
	j = json.loads(p)
	# pprint(j.keys())
	# pprint(dir(j))
	# pprint(j.items())
	# pprint(j.viewkeys())
	# pprint(j['data']['children'])
	pprint(j.keys())
	pprint(j['data'].keys())
	pprint(j['data']['children'][0].keys())
	pprint(j['data']['children'][0]['data'].keys())
	pprint(j['data']['children'][0]['data']['ups'])
	# pprint(sum(i['data']['ups'] for i in j['data']['children']))
	return p



if __name__ == "__main__":
	parse_reddit_json()

	