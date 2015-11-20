#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

__title__ = 'opennms-client'
__version__ = '0.1'
__author__ = 'Manuel Villarejo'
__author_email__ = 'mjvillarejo@gmail.com'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2015 Manuel Villarejo'

packages = [
    __title__
]

with open('requirements.txt') as f:
    requires = f.read().splitlines()


setup(
    name="opennms-client",
    version= __version__,
    description="",
    long_description=read('README.rst'),
    url='https://github.com/mvillarejo/%s' % __title__,
    license=__license__,
    author=__author__,
    author_email=__author_email__,
    download_url='https://github.com/mvillarejo/%s/releases' % __title__,
    bugtrack_url='https://github.com/mvillarejo/%s/issues' % __title__,
    platforms='any',
    keywords='%s opennms client python' % __title__,
    package_data={'': ['LICENSE']},
    package_dir={__title__: __title__},
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requires,
    tests_require=[],
        classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
