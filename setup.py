#!/usr/bin/python

from setuptools import setup

setup(
    name = 'servicenow',
    version = '0.0.1',
    description = 'A library to manage data in the Service Now database',
    long_description = 'A library to manage Incidents, Service Requests, CMDB Items in the Service Now database',
    maintainer = 'Juliano Martinez',
    maintainer_email = 'juliano.martinez@locaweb.com.br',
    package_dir={'servicenow': 'src/lib'},
    packages=['servicenow'],
    licence = 'Apache',
)
