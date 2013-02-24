from setuptools import setup, find_packages
import sys

assert sys.version_info >= (3,), 'pycodejam is a python 3 compatible library.'

setup(
    name = "pycodejam",
    version = "1.0.0",
    packages = find_packages('src', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir = { '': 'src' },
    test_suite = 'codejam.tests',

    # metadata for upload to PyPI
    author = "Jon Eisen",
    author_email = "jon.m.eisen@gmail.com",
    description = "This module provides helpers to run and parse CodeJam problems",
    license = "MIT",
    keywords = "google code jam codejam competition problem",
)
