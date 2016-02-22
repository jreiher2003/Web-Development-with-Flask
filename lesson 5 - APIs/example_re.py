import re

# p = re.compile('ab*')
# print p
# q = re.compile('ab*', re.IGNORECASE)
# print q
# r = re.compile('[a-zA-Z]+')
# print r
# print r.match('')
# m = r.match('tempo')
# print m.group()
# print m.start()
# print m.end()
# print m.span()


def func():
	# p = re.compile('[a-zA-Z0-9_]')
	p = re.compile('\d+')
	m = p.search('The  string you want to 129999 match or check to see 76 99 that it is not None')
	if m:
		print 'Match found: ', m.group(), m.span()
	else:
		print 'You were searching for a number and didn\'t find one'

def func_grouping():
	p = re.compile('(a)b')
	m = p.match('ab')
	print m.group(1)

def func1():
	p = re.compile('\d+')
	print p.findall('We are 12 going 41 findall 888 numbers')


def func2():
	p = re.compile('\d+')
	i = p.finditer('I have 38 thirty-eights about 9 nines 10 tens')
	for match in i:
		print match.group(1),match.span()

def func3():
	print re.match(r'From\s+', 'Fromage amk')
	print re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998').group()

def func4():
	charref = re.compile(r"""
		&[#] # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
	charref1 = re.compile("&#(0[0-7]+"
                     "|[0-9]+"
                     "|x[0-9a-fA-F]+);")




if __name__ == '__main__':
	# func()
	func_grouping()
	# func1()
	# func2()
	# func3()
	# func4()