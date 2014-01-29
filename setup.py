#!/usr/bin/python

from setuptools import setup

setup(
    name = 'servicenow',
    version = '1.0.1',
    description = 'Python Library to interact and manage the ServiceNow database',
    long_description = 'Python Library to interact and manage the ServiceNow database',
    maintainer = 'Juliano Martinez',
    maintainer_email = 'juliano.martinez@locaweb.com.br',
    package_dir={'servicenow': 'src/lib'},
    packages=['servicenow'],
    license = 'Apache',
)
