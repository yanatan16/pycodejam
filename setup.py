from setuptools import setup, find_packages
import sys

setup(
    name = "pycodejam",
    version = "1.2.0",
    packages = find_packages('src', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir = { '': 'src' },
    test_suite = 'codejam.tests',

    # metadata for upload to PyPI
    author = "Jon Eisen",
    author_email = "jon.m.eisen@gmail.com",
    description = "This module provides helpers to run and parse CodeJam problems",
    url = "http://github.com/yanatan16/pycodejam",
    license = "MIT",
    keywords = "google code jam codejam competition problem",
    zip_safe = True
)
