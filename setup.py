#!/usr/bin/env python
import os

from setuptools import setup, find_packages

VERSION = 0.1
version = os.path.join('onedns', '__init__.py')
execfile(version)

README = open('README.md').read()

setup(
    name='onedns',
    version=VERSION,
    packages=find_packages(),
    author='Justin Riley',
    author_email='justin.t.riley@gmail.com',
    url="https://github.com/fasrc/onedns",
    description="Dynamic DNS for OpenNebula",
    long_description=README,
    install_requires=[
        "oca>=4.10.0",
        "python-etcd>=0.4.3",
    ],
    entry_points=dict(console_scripts=['onedns = onedns.cli:main']),
    zip_safe=False
)