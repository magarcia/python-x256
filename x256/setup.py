#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

HERE = os.path.dirname(__file__)

setup(name = "x256",
    version = '0.1',
    description = "x256: manipulate xterm 256 color codes",
    author = "Martin Garcia",
    author_email = "newluxfero@gmail.com",
    license = "MIT",
    url = "https://github.com/magarcia/python-x256",
    packages = ["x256"],
    platforms = ["POSIX", "Windows"],
    long_description = open(os.path.join(HERE, "README.md"), "r").read(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ],
)
