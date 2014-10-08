import hashlib
import json
import redis

from functools import wraps

rd = redis.Redis()
def cached(ttl=300):
    def proxy(f):
        @wraps(f)
        def caching(*args, **kwargs):
            if ttl == 0:
                return f(*args, **kwargs)

            _hash = "%s-%s" % (f.__name__, hashlib.md5("%s%s" % (
                repr(args[1:]),
                repr(kwargs)
            )).hexdigest())
            try:
                cache = rd.get(_hash)
                if not cache:
                    cache = json.dumps(f(*args, **kwargs))
                    rd.setex(_hash, cache, ttl)
                return json.loads(cache)
            except Exception, e:
                return f(*args, **kwargs)
        return caching
    return proxy

def format_query(meta={}, metaon={}):
    query = '^'.join(['%s=%s' % (field, value) for field, value in meta.iteritems()])
    if metaon:
        query += '^' + '^'.join(['%sON%s' % (field, value) for field, value in metaon.iteritems()])
    return query
