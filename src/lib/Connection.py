import json
import logging
import requests

class Auth(object):
    """
    Creates the connection to be used on each request to servicenow
    """

    def __init__(self, username, password, instance, debug=False):
        """
        Receives the username and password to authenticate the user
        The instance argument is the path of your account on servicenow

        Example:

        >>> conn = Connection.Auth(username="juliano.martinez", password="P4SsW0rD", instance="locaweb")
        """
        self.username = username
        self.password = password

        if 'https://' in instance:
            self.instance = instance
        else:
            self.instance = 'https://%s.service-now.com/' % instance

        self.session = requests.Session()
        self.session.auth = (self.username, self.password)

    def _get(self, table, meta, metaon=None):
        query = '^'.join(['%s=%s' % (field, value) for field, value in meta.iteritems()])
        if metaon:
            query += '^' + '^'.join(['%sON%s' % (field, value) for field, value in metaon.iteritems()])
        params = {'JSON':'', 'sysparm_action': 'getRecords', 'sysparm_query': query}
        return self.session.get('%s/%s' % (self.instance, table), params=params)

    def _post(self, table, params):
        return self.session.post('%s/%s?JSON&sysparm_action=insert' % (self.instance, table), params=json.dumps(params))

    def _update(self, table, where, params):
        query = '^'.join(['%s=%s' % (field, value) for field, value in where.iteritems()])
        return self.session.post('%s/%s?JSON&sysparm_query=%s&sysparm_action=update' % (self.instance, table, query), params=json.dumps(params))

    def _delete(self, table, params):
        if not 'sysparm_sys_id' in params:
            raise IndexError('You must use sysparm_sys_id=<id> to delete')
        return self.session.post('%s/%s?JSON&sysparm_action=deleteRecord' % (self.instance, table), params=json.dumps(params))
