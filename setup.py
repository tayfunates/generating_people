#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
The setup script for this project.
@author: Christoph Lassner
"""
from setuptools import setup
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

VERSION = '0.1'
REQS = [str(ir.req) for ir in parse_requirements('requirements.txt',
                                                 session='tmp')]

setup(
    name='gp_tools',
    author='Christoph Lassner',
    author_email='mail@christophlassner.de',
    packages=['gp_tools'],
    dependency_links=['http://github.com/classner/clustertools/tarball/master#egg=clustertools'],
    include_package_data=True,
    install_requires=REQS,
    version=VERSION,
    license='Creative Commons Non-Commercial 4.0',
)
