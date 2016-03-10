import time

##### my answer #############
def complex_computation(a, b):
    time.sleep(.5)
    return a + b

cache = {}
def cached_computation(a,b):
    key = "key"
    try:
        if cache[key]:
            cache
    except KeyError:
        cache[key] = complex_computation(a,b)
    return cache

#### udacity's answer 
cache2 = {}
def cached_computation_u(a,b):
    key = (a,b)
    if key in cache2:
        r = cache2[key]
        print r
    else:
        r = complex_computation(a,b)
        cache2[key] = r
        print cache2[key]
    print r
    return r


if __name__ == "__main__":
    start_time = time.time()
    cached_computation(2,2)
    print "the first computation took %f seconds" % (time.time() - start_time)
    print "\n"

    start_time_2 = time.time()
    cached_computation(2,2)
    print "the second computation took %f seconds" % (time.time() - start_time_2)
    print "\n"

    start_time3 = time.time()
    cached_computation_u(2,2)
    print "the third computation took %f seconds" % (time.time() - start_time3)
    print "\n"

    start_time_4 = time.time()
    cached_computation_u(2,2)
    print "the fourth computation took %f seconds" % (time.time() - start_time_4)
    print "\n"
