from setuptools import setup, find_packages
import sys

assert sys.version_info >= (3,), 'pycodejam is a python 3 compatible library.'

setup(
    name = "pycodejam",
    version = "0.1",
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    test_suite = 'codejam.tests',

    # metadata for upload to PyPI
    author = "Jon Eisen",
    author_email = "jon.m.eisen@gmail.com",
    description = "This module provides helpers to run and parse CodeJam problems",
    license = "MIT",
    keywords = "google code jam codejam competition problem",
)