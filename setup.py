#!/usr/bin/python

from setuptools import setup

setup(
    author = 'Juliano Martinez',
    author_email = 'juliano.martinez@locaweb.com.br',
    name = 'servicenow',
    version = '1.0.1',
    url = 'https://github.com/locaweb/python-servicenow',
    description = 'Python Library to interact with and manage the ServiceNow database',
    install_requires = ['requests','redis'],
    long_description = open('README.md').read(),
    maintainer = 'Francisco Freire',
    maintainer_email = 'francisco.freire@locaweb.com.br',
    package_dir = {'servicenow': 'src/lib', 'servicenow.drivers': 'src/lib/drivers'},
    packages = ['servicenow', 'servicenow.drivers'],
    license = 'Apache',
)
