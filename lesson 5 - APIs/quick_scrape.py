import urllib2
import re
from bs4 import BeautifulSoup as bs
from pprint import pprint

EMAIL_ADDRESS = re.compile('\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Z]{2,}\b')
EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

def parse_me():
# p = urllib2.urlopen('http://www.prediction.com')
    p = urllib2.urlopen('http://www.usyouthsoccer.org/englewood_soccer_association/')
    x = p.read()
    # print x
    email = re.findall(EMAIL_ADDRESS, x)
    print email
    print len(email)

def parse_me1():
    p = urllib2.urlopen('http://www.usyouthsoccer.org/englewood_soccer_association/')
    x = p.read()
    i = EMAIL_RE.finditer(x)
    for match in i:
        print match.group(), match.span()

def parse_me2():
	p = urllib2.urlopen('http://www.usyouthsoccer.org/englewood_soccer_association/')
	x = p.read()
	print re.match('keithsoccer@gmail.com', x)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

def valid_email(email):
    p = urllib2.urlopen('http://www.usyouthsoccer.org/englewood_soccer_association/')
    x = p.read()
    print x

# EMAIL_RE1 = 'keithsoccer@gmail.com'
def grab_email(url):
    p = urllib2.urlopen(url)
    # pprint(dir(p))
    print p.url
    f = p.read()
    m = EMAIL_RE.match('keithsoccer@gmail.com')
    if m:
    	print 'match found: ', m.group()
    else:
    	print 'no match found'
    # files1 = EMAIL_RE1.search(files)
    # print files1

def grab_email1(url):
	p = urllib2.urlopen(url)
	# print p.read()
	# f = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+')
	EMAIL_ADDRESS = re.compile(r'\b[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+')

	# pprint(f.findall(p.read()))
	pprint(EMAIL_ADDRESS.findall(p.read()))

if __name__ == '__main__':
	# parse_me()
	# parse_me1()
	# parse_me2()
	# valid_email('keithsoccer@gmail.com')
	grab_email1('http://www.usyouthsoccer.org/englewood_soccer_association/')