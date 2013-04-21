#!/usr/bin/env python3
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name="megaclient",
    version="0.1",
    author='Tomáš Heřman',
    author_email='tomas.herman@gmail.com',
    packages=["megaclient"],
    url='http://www.github.com/tomasherman/megaclient',
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    requires = [
        'distribute',
        "mega.py (>= 0.9.5)"
    ],
    entry_points = {
        'console_scripts' : [
            ['megaclient = megaclient.megaclient:main']
        ]
    }
)
