#!/usr/bin/env python3
from distutils.core import setup

setup(
    name="mega-client",
    version="0.1",
    author='Tomáš Heřman',
    author_email='tomas.herman@gmail.com',
    packages=["mega-client"],
    url='http://www.github.com/tomasherman/mega-client',
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    requires = [
        "mega.py (>= 0.9.5)"
    ]
)
