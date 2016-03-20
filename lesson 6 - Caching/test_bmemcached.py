import bmemcached

servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
user = os.environ.get('MEMCACHIER_USERNAME', '')
password = os.environ.get('MEMCACHIER_PASSWORD', '')

# development
mc = bmemcached.Client(('127.0.0.1:11211', ), 'user',
                            'password')
# production
mc = bmemcached.Client(servers, binary=True,
                    username=user, password=password,
                    behaviors={
                      # Faster IO
                      "tcp_nodelay": True,
                      "no_block": True,

                      # Timeout for set/get requests
                      "_poll_timeout": 2000,

                      # Use consistent hashing for failover
                      "ketama": True,

                      # Configure failover timings
                      "connect_timeout": 2000,
                      "remove_failed": 4,
                      "retry_timeout": 2,
                      "dead_timeout": 10,
                    })

mc.set('key', 'value')
print mc.get('key')