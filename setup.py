#!/usr/bin/env python

from setuptools import (
    Command,
    find_packages,
    setup,
)
import sys


install_requires = [
    'twitterbot>=0.3.2',
]

setup_requires = []

test_require = [

]

if 'nosetests' in sys.argv[1:]:
    setup_requires.extend(tests_require)

setup(name='CramerAdvice',
    version='1.0',
    description='Life advice from an expert',
    author='James Greenhill',
    author_email='fuziontech@gmial.com',
    url='https://www.crameradvice.com/',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=install_requires,
    setup_requires=setup_requires,
    license='MIT'
    )

