#!/usr/bin/env python
from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='yaww',
      version=version,
      description="Yet Another Work launching Wrapper",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Python Scheduling Pipeline',
      author='Johannes Alneberg',
      author_email='johannes.alneberg@scilifelab.se',
      url='https://github.com/alneberg/yaww',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts=["bin/yaww"],
      include_package_data=True,
      zip_safe=False,
      install_requires=['nose==1.3.0'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

