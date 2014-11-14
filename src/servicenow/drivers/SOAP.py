import urllib

from SOAPpy import SOAPProxy
from servicenow import Connection, Utils

class NotImplemented:
    pass

class Auth(Connection.Auth):

    def __init__(self, username, password, instance, timeout=60, debug=False):
        self.username = username
        self.password = password
        self.instance = instance

    def _get_proxy(self, table, params={}):
        params['SOAP'] = ''
        return SOAPProxy('https://%s:%s@%s.service-now.com/%s?%s' % (self.username, self.password, self.instance, table, urllib.urlencode(params)), 'http://www.service-now.com/')

    def _get(self, table, meta, metaon={}, params={}, extended={}):
        server = self._get_proxy(table, params)
        return server.getRecords(__encoded_query=Utils.format_query(meta, metaon), **extended)

    def _list(self, table, meta, metaon={}, params={}, extended={}):
        server = self._get_proxy(table, params)
        return server.getKeys(__encoded_query=Utils.format_query(meta, metaon), **extended)

    def _list_by_query(self, table, query, params={}, extended={}):
        server = self._get_proxy(table, params)
        return server.getKeys(__encoded_query=query, **extended)

    def _get_by_query(self, table, query, params={}, extended={}):
        server = self._get_proxy(table, params)
        return server.getRecords(__encoded_query=query, **extended)

    def _post(self, table, data, params={}):
        raise NotImplemented

    def _post_multiple(self, table, data, params={}):
        raise NotImplemented

    def _update(self, table, where, data, params={}):
        raise NotImplemented

    def _update_by_query(self, table, query, data):
        raise NotImplemented

    def _delete(self, table, id, params={}, extended={}):
        raise NotImplemented

    def _delete_multiple(self, table, query, params={}):
        raise NotImplemented

    def _format(self, response):
        if len(response) == 1:
            return [response, ]
        else:
            return response
