import requests
import logging
import json

class Auth(object):
    def __init__(self, username, password, instance, debug=False):
        self.username = username
        self.password = password
        if 'https://' in instance:
            self.instance = instance
        else:
            self.instance = 'https://%s.service-now.com/' % instance
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)

    def _get(self, table, meta):
        query = '^'.join(['%s=%s' % (field, value) for field, value in meta.iteritems()])
        params = {'JSON':'', 'sysparm_action': 'getRecords', 'sysparm_query': query}
        return self.session.get('%s/%s' % (self.instance, table), params=params)

    def _post(self, table, params):
        return self.session.post('%s/%s?JSON&sysparm_action=insert' % (self.instance, table), params=json.dumps(params))

    def _update(self, table, params):
        return self.session.post('%s/%s?JSON&sysparm_action=update' % (self.instance, table), params=json.dumps(params))

    def _delete(self, table, params):
        if not 'sysparm_sys_id' in params:
            raise IndexError('You must use sysparm_sys_id=<id> to delete')
        return self.session.post('%s/%s?JSON&sysparm_action=deleteRecord' % (self.instance, table), params=json.dumps(params))
