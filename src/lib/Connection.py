import requests
import logging

class Auth(object):
    def __init__(self, username, password, instance, debug = False):
        self.username = username
        self.password = password
        if 'https://' in instance:
            self.instance = instance
        else:
            self.instance = 'https://%s.service-now.com/' % instance
        requests.get(self.instance, auth=(self.username, self.password))

    def _get(self, url, params):
        if '?' in url:
            return requests.get("%s/%s&JSON" % (self.instance, url), params=params)
        else:
            return requests.get("%s/%s?JSON" % (self.instance, url), params=params)
