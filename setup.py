#!/usr/bin/env python
from packageversion import PackageVersion
from setuptools import setup, find_packages

pv = PackageVersion()
v = pv.generate_next_stable(package_name='packageversion')

setup(name='packageversion',
      version=v,
      description='Library to generate python package version for CI',
      author='Jon Skarpeteig',
      author_email='jon.skarpeteig@gmail.com',
      url='https://github.com/Yuav/python-packageversion',
      packages=find_packages(),
      install_requires=[
          'semantic_version',
          'flexmock'
      ]
      )
