import itertools
from pprint import pprint

SERVERS = ['SERVER1', 'SERVER2', 'SERVER3', 'SERVER4']

def get_server():
    cycle_servers = itertools.cycle(SERVERS)
    i = 0
    for value in cycle_servers:
        print value
        i += 1
        if i >= 4:
            break
    # print cycle_servers.next()
    # print cycle_servers.next()
    # print cycle_servers.next()
    # print cycle_servers.next()
n = -1
def get_server_u():
    global n
    n += 1
    return SERVERS[n % len(SERVERS)]

        

    

# pprint(dir(get_server()))
# pprint(get_server())
# pprint(get_server())
# pprint(get_server())
# pprint(get_server())

print get_server_u()
print get_server_u()
print get_server_u()
print get_server_u()
