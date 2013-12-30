import requests
import logging
import json

class Auth(object):
    def __init__(self, username, password, instance, timeout=60, debug=False):
        self.username = username
        self.password = password
        if 'https://' in instance:
            self.instance = instance
        else:
            self.instance = 'https://%s.service-now.com/' % instance
        self.timeout = timeout
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)

    def _list(self, table, meta, metaon=None):
        query = '^'.join(['%s=%s' % (field, value) for field, value in meta.iteritems()])
        if metaon:
            query += '^' + '^'.join(['%sON%s' % (field, value) for field, value in metaon.iteritems()])
        params = {'JSON':'', 'sysparm_action': 'getKeys', 'sysparm_query': query}
        return self.session.get('%s/%s' % (self.instance, table), params=params, timeout=self.timeout)

    def _list_by_query(self, table, query):
        params = {'JSON': '', 'sysparm_action': 'getKeys', 'sysparm_query': query}
        return self.session.get('%s/%s' % (self.instance, table), params=params, timeout=self.timeout)

    def _get(self, table, meta, metaon=None, displayvalue=False, displayvariables=False):
        query = '^'.join(['%s=%s' % (field, value) for field, value in meta.iteritems()])
        if metaon:
            query += '^' + '^'.join(['%sON%s' % (field, value) for field, value in metaon.iteritems()])
        params = {'JSON':'', 'sysparm_action': 'getRecords', 'sysparm_query': query}
        if displayvalue:
            params['displayvalue'] = 'true'
        if displayvariables:
            params['displayvariables'] = 'true'
        return self.session.get('%s/%s' % (self.instance, table), params=params, timeout=self.timeout)

    def _post(self, table, params):
        return self.session.post('%s/%s?JSON&sysparm_action=insert' % (self.instance, table), params=json.dumps(params), timeout=self.timeout)

    def _update(self, table, where, params):
        query = '^'.join(['%s=%s' % (field, value) for field, value in where.iteritems()])
        return self.session.post('%s/%s?JSON&sysparm_query=%s&sysparm_action=update' % (self.instance, table, query), params=json.dumps(params), timeout=self.timeout)

    def _delete(self, table, params):
        if not 'sysparm_sys_id' in params:
            raise IndexError('You must use sysparm_sys_id=<id> to delete')
        return self.session.post('%s/%s?JSON&sysparm_action=deleteRecord' % (self.instance, table), params=json.dumps(params), timeout=self.timeout)
