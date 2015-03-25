# coding: utf-8
from uuid import uuid1
from setuptools import setup,  find_packages
from pip.req import parse_requirements

setup(
    name='vmmaster-client',
    version='0.1',
    description='vmmaster client for additional vmmaster api',
    url='https://github.com/nwlunatic/vmmaster-client',
    packages=find_packages(),
    install_requires=[
        'requests==2.3.0',
    ])
