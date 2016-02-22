import urllib2
from pprint import pprint

# p = urllib2.urlopen('http://www.prediction.com')
p = urllib2.urlopen('http://www.example.com')
pprint(dir(p))
# print p.url()
# print p.fp
print p.url
print p.msg 
print p.headers
print p.getcode()
# print p.info()
# print p.geturl
# print p.fileno