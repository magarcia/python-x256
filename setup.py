#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

HERE = os.path.dirname(__file__)

setup(
    name = "x256",
    version = '0.0.2',
    description = "x256: manipulate xterm 256 color codes",
    author = "Martin Garcia",
    author_email = "newluxfero@gmail.com",
    license = "MIT",
    url = "https://github.com/magarcia/python-x256",
    packages = ["x256"],
    platforms = "POSIX",
    long_description = ("x256 can convert colors from rgb or hex to xterm 256 "
                        "colors, and convert colors from xterm 256 colors to "
                        "rgb or hex. "),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
)
