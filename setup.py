#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__title__ = 'opennms-client'
__version__ = '0.1'
__author__ = 'Manuel Villarejo'
__author_email__ = 'mjvillarejo@gmail.com'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2015 Manuel Villarejo'

packages = [
    # __title__ # TODO: use something more standard
    "client"
]

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

requires = []
with open('requirements.txt') as f:
    requires = f.read().splitlines()

with open('README.rst') as f1:
    with open('CHANGELOG.rst') as f2:
        long_desc = f1.read() + '\n\n' + f2.read()


setup(
    name=__title__,
    version= __version__,
    description="",
    long_description=long_desc,
    url='https://github.com/mvillarejo/%s' % __title__,
    license=__license__,
    author=__author__,
    author_email=__author_email__,
    download_url='https://github.com/mvillarejo/%s/releases' % __title__,
    bugtrack_url='https://github.com/mvillarejo/%s/issues' % __title__,
    platforms='any',
    keywords='%s opennms client python' % __title__,
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={__title__: __title__},
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
    extras_require={
        'security': ['pyOpenSSL>=0.15.1', 'ndg-httpsclient', 'pyasn1'],
    },
)
