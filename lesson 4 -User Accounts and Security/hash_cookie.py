import hashlib

def hash_str(s):
	return hashlib.md5(s).hexdigest()

# print hash_str('foobar')


def make_secure_val(s):
	return "%s, %s" % (s, hash_str(s))

# print make_secure_val('foobar')


def check_secure_val(s):
	val = s.split(',')[0].strip()
	hash_val = s.split(',')[1].strip()
	check_val =  make_secure_val(val).split(',')[1].strip()
	if hash_val == check_val:
		return val
	else:
		return None

print check_secure_val('foobar, 3858f62230ac3c915f300c664312c63f')




s = 'foobar, 3858f62230ac3c915f300c664312c63f'
val = s.split(',')[0].strip()
hash_val = s.split(',')[1].strip()
check_val =  make_secure_val(val).split(',')[1].strip()
# print [ HASH.split(',')[0].strip() if hash_str('foobar') == HASH.split(',')[1].strip() else None ][0]
print [val if hash_val == check_val else None][0]