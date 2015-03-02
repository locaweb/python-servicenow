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
            except Exception:
                return f(*args, **kwargs)
        return caching
    return proxy

def format_query(meta={}, metaon={}):
    try:
        items = meta.iteritems()
        if metaon:
            metaon_items = metaon.iteritems()
    except AttributeError:
        items = meta.items()
        if metaon:
            metaon_items = metaon.items()

    query = '^'.join(['%s=%s' % (field, value) for field, value in items])
    if metaon:
        query += '^' + '^'.join(['%sON%s' % (field, value) for field, value in metaon_items])
    return query
