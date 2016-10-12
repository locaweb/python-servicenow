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

            _hash = "{0}-{1}".format(f.__name__, hashlib.md5("{0}{1}".format(
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


def format_query_type(value):
    if type(value) in (type([]), type(())):
        return ('IN', ','.join(value))
    else:
        return ('=', value)


def format_query(meta={}, metaon={}):
    try:
        items = meta.items()
        if metaon:
            metaon_items = metaon.items()
    except AttributeError:
        items = meta.items()
        if metaon:
            metaon_items = metaon.items()

    query = '^'.join(['{0}{1}{2}'.format(
        field, format_query_type(value)[0],
        format_query_type(value)[1]) for field, value in items])
    if metaon:
        query += '^' + '^'.join(['{0}ON{1}'.format(field, value)
                                 for field, value in metaon_items])
    return query
