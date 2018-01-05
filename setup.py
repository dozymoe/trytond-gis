#!/usr/bin/env python
# This file is part of trytond_gis.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import io
import os
import re
from setuptools import setup, find_packages


def read(fname):
    return io.open(
        os.path.join(os.path.dirname(__file__), fname),
        'r', encoding='utf-8').read()


def get_require_version(name):
    if minor_version % 2:
        require = '%s >= %s.%s.dev0, < %s.%s'
    else:
        require = '%s >= %s.%s, < %s.%s'
    require %= (name, major_version, minor_version,
        major_version, minor_version + 1)
    return require


def get_version():
    init = read(os.path.join('trytond_gis', '__init__.py'))
    return re.search('__version__ = "([0-9.]*)"', init).group(1)

version = get_version()
major_version, minor_version, _ = version.split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)
name = 'trytond_gis'

download_url = 'http://downloads.tryton.org/%s.%s/' % (
    major_version, minor_version)
if minor_version % 2:
    version = '%s.%s.dev0' % (major_version, minor_version)
    download_url = 'hg+http://hg.tryton.org/%s#egg=%s-%s' % (
        name, name, version)

requires = ['geomet', get_require_version('trytond')]

tests_require = ['mock']
dependency_links = []
if minor_version % 2:
    dependency_links.append('https://trydevpi.tryton.org/')


setup(name=name,
    version=version,
    description='Adds Geographic Information System support to trytond',
    long_description=read('README'),
    author='Tryton',
    author_email='issue_tracker@tryton.org',
    url='http://www.tryton.org/',
    download_url=download_url,
    keywords='tryton GIS',
    packages=find_packages(),
    classifiers=[
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    platforms='any',
    license='GPL-3',
    install_requires=requires,
    entry_points={
        'trytond.backend': [
            'postgis = trytond_gis.postgis',
            ],
        'trytond.tests': [
            'test_geographic_fields = trytond_gis.tests',
            ],
        },
    zip_safe=False,
    test_suite='trytond.tests',
    test_loader='trytond.test_loader:Loader',
    tests_require=tests_require,
    use_2to3=True,
    )