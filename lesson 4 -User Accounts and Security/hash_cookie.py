import hashlib

def hash_str(s):
	return hashlib.md5(s).hexdigest()

print hash_str('foobar')


def make_secure_val(s):
	return "%s, %s" % (s, hash_str(s))

print make_secure_val('foobar')