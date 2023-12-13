#!/usr/bin/env python
"""Setup script."""
from setuptools import setup, find_packages

setup(
    name='brendapy',
    version='0.5.0',
    description='Brenda parser in python',
    license='LGPL-3.0',
    author='matthiaskoenig',
    author_email='konigmatt@googlemail.com',
    setup_requires=['pytest-runner',], # instead of: setup_requires=['pytest-runner'], 
    tests_require=['pytest',],
    packages=find_packages(),
    include_package_data=True,
    keywords=['brendapy'],
    url='https://github.com/matthiaskoenig/brendapy',
    classifiers=['',]
)