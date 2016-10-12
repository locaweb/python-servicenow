import requests
import json

from . import Utils


class Auth(object):

    def __init__(self, username, password, instance, timeout=60,
                 debug=False, api='JSON', proxies={}, verify=True):
        self.username = username
        self.password = password
        if 'https://' in instance:
            self.instance = instance
        else:
            self.instance = 'https://{0}.service-now.com/'.format(instance)
        self.timeout = timeout
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)
        self.api = api
        self.proxies = proxies
        self.verify = verify
        if api.startswith('JSON'):
            self.session.headers.update({'Accept': 'application/json'})

    def _list(self, table, meta={}, **kwargs):
        query = Utils.format_query(meta, kwargs.get('metaon', {}))
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'getKeys',
            'sysparm_query': query
        })
        return self.session.get('{0}/{1}'.format(self.instance, table),
                                params=params, timeout=self.timeout,
                                proxies=self.proxies, verify=self.verify)

    def _list_by_query(self, table, query, **kwargs):
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'getKeys',
            'sysparm_query':    query
        })
        return self.session.get('{0}/{1}'.format(self.instance, table),
                                params=params, timeout=self.timeout,
                                proxies=self.proxies, verify=self.verify)

    def _get(self, table, meta={}, **kwargs):
        query = Utils.format_query(meta, kwargs.get('metaon', {}))
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'getRecords',
            'sysparm_query': query
        })
        return self.session.get('{0}/{1}'.format(self.instance, table),
                                params=params, timeout=self.timeout,
                                proxies=self.proxies, verify=self.verify)

    def _get_by_query(self, table, query, **kwargs):
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'getRecords',
            'sysparm_query': query
        })
        return self.session.get('{0}/{1}'.format(self.instance, table),
                                params=params, timeout=self.timeout,
                                proxies=self.proxies, verify=self.verify)

    def _post(self, table, data, **kwargs):
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'insert'
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, data=json.dumps(data),
                                 timeout=self.timeout, proxies=self.proxies,
                                 verify=self.verify)

    def _post_multiple(self, table, data, **kwargs):
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'insertMultiple'
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, data=json.dumps(data),
                                 timeout=self.timeout, proxies=self.proxies,
                                 verify=self.verify)

    def _update(self, table, where, data, **kwargs):
        query = Utils.format_query(where, {})
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'update',
            'sysparm_query':    query
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, data=json.dumps(data),
                                 timeout=self.timeout, proxies=self.proxies,
                                 verify=self.verify)

    def _update_by_query(self, table, query, data, **kwargs):
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'update',
            'sysparm_query':    query
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, data=json.dumps(data),
                                 timeout=self.timeout, proxies=self.proxies,
                                 verify=self.verify)

    def _delete(self, table, id, **kwargs):
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'deleteRecord',
            'sysparm_sys_id':    id
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, timeout=self.timeout,
                                 proxies=self.proxies, verify=self.verify)

    def _delete_multiple(self, table, query, **kwargs):
        params = kwargs.get('params', {})
        params.update({
            self.api:             '',
            'sysparm_action':   'deleteMultiple',
            'sysparm_query':    query
        })
        return self.session.post('{0}/{1}'.format(self.instance, table),
                                 params=params, timeout=self.timeout,
                                 proxies=self.proxies, verify=self.verify)

    def _format(self, response):
        return json.loads(response.text)
