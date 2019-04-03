"""
Dragon name: a silly code demo
"""

from setuptools import setup, find_packages

import unittest

def load_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test*.py')
    return test_suite

setup(
    name='dragons',
    version='0.0.1',
    description=('Discover your dragon name'),
    license='MIT',
    test_suite='setup.load_test_suite',
    packages=find_packages(),
    entry_points={'console_scripts': ['dragon-name = dragons:main']}
    )
