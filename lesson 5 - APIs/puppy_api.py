import requests
from pprint import pprint

def pup_api():
    url = "http://adopt-puppy.herokuapp.com/shelters/.json"
    response = requests.get(url)
    shelters = response.json()
    for key, value in shelters.items():
    	# print key, value[0]['name']
    	for v in value:
    		print v['name']

# pprint(type(pup_api()))
pprint(pup_api())