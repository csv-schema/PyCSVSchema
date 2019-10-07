#!/usr/bin/python
# -*-coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open('README_pypi.rst') as f:
    long_description = f.read()

setup(
    name='pycsvschema',
    version='0.0.4',
    description='PyCSVSchema is an implementation of CSV Schema in Python.',
    long_description=long_description,
    author='Guangyang Li',
    author_email='mail@guangyangli.com',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='csv schema json jsonschema validation validator',
    url='https://github.com/crowdskout/PyCSVSchema',
    install_requires=["jsonschema", "rfc3986"],
)
