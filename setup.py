#!/usr/bin/env python
# -*- coding:utf-8 -*-

from distutils.core import setup

from strings._version import __author__, __email__, __homepage__, __version__


def read(path):
    with open(path) as f:
        return f.read()


setup(
    name='strings-parser',
    description="A simple parser for Apple's localizable strings parser",
    url=__homepage__,
    long_description=read('README.rst'),
    version=__version__,
    author=__author__,
    author_email=__email__,
    packages=['strings'],
)
