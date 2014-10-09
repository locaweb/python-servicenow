import unittest
import getpass

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

from servicenow import ServiceNow
from servicenow import Connection

instance = raw_input('Enter SN instance: ')
username = raw_input('Enter SN username: ')
password = getpass.getpass('Enter password: ')

incident = {'short_description': 'automated test', 'description': 'automated test'}

class TestSequenceFunctions(unittest.TestCase):
    conn = Connection.Auth(username=username, password=password, instance=instance, api='JSONv2')
    inc = ServiceNow.Incident(conn)
    incident = {}

    def test_00_insert(self):
        global incident
        createdinc = self.inc.create({'short_description': 'automated test', 'description': 'automated test'})
        self.assertTrue('number' in createdinc['records'][0])
        incident = createdinc['records'][0]

    def test_02_update(self):
        global incident
        text = 'updated'
        updated = self.inc.update({'number': incident['number']}, {'short_description': 'updated'})
        self.assertEqual(text, updated['records'][0]['short_description'])
        incident = updated['records'][0]

    def test_02_fetch_one(self):
        global incident
        self.assertEqual(self.inc.fetch_one({'number': incident['number']}), incident)

    def test_03_fetch_all(self):
        global incident
        self.assertEqual(self.inc.fetch_all({'number': incident['number']})['records'][0], incident)

    def test_04_delete(self):
        global incident
        deleted = self.inc.delete(incident['sys_id'])
        self.assertEqual(incident, deleted['records'][0])

if __name__ == '__main__':
    unittest.main()
