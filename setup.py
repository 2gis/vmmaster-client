# coding: utf-8
from uuid import uuid1
from setuptools import setup,  find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt", session=uuid1())
requirements = [str(ir.req) for ir in install_reqs]

setup(
    name='vmmaster-client',
    version='0.1',
    description='vmmaster client for additional vmmaster api',
    url='https://github.com/nwlunatic/vmmaster-client',
    packages=find_packages(),
    install_requires=[
        'requests==2.3.0',
    ])
