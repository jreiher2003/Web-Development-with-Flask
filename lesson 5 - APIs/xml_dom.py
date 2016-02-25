from xml.dom import minidom
import urllib2 
from pprint import pprint

p = urllib2.urlopen('http://www.nytimes.com/services/xml/rss/nyt/GlobalHome.xml')

y = minidom.parseString(p.read())
z = y.getElementsByTagName('item')
pprint(len(z))