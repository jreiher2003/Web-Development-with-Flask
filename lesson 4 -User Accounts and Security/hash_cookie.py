import hashlib

def hash_str(s):
	return hashlib.md5(s).hexdigest()

print hash_str('foobar')


def make_secure_val(s):
	return "%s, %s" % (s, hash_str(s))

print make_secure_val('foobar')


def check_secure_val(s):
	HASH = make_secure_val(s)
	if hash_str(s) == HASH.split(',')[1].strip():
		return HASH.split(',')[0].strip() 
	else:
		return None
	# print HASH.split(',')[1].strip()


print check_secure_val('foobar')


HASH = make_secure_val('foobar')
print [ HASH.split(',')[0].strip() if hash_str('foobar') == HASH.split(',')[1].strip() else None ][0]