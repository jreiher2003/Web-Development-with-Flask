import urllib2
from pprint import pprint

p = urllib2.urlopen('http://www.prediction.com')
pprint(dir(p))
# print p.url()
# print p.fp
print p.url
print p.msg 
print p.headers
print p.getcode()
print p.info()
# print p.geturl
# print p.fileno