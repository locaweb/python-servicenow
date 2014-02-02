#!/usr/bin/python

from setuptools import setup

setup(
    author = 'Juliano Martinez',
    author_email = 'juliano.martinez@locaweb.com.br',
    name = 'servicenow',
    version = '1.0.1',
    url = 'https://github.com/locaweb/python-servicenow'
    description = 'Python Library to interact with and manage the ServiceNow database',
    long_description = open('README.md').read()
    maintainer = 'Juliano Martinez',
    maintainer_email = 'juliano.martinez@locaweb.com.br',
    package_dir = {'servicenow': 'src/lib'},
    packages = ['servicenow'],
    license = 'Apache',
)
