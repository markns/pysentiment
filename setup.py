#!/usr/bin/python

from setuptools import setup

setup(name='pysentiment',
      version='0.1.2a',
      description='Python sentiment analysis utilities',
      author='Zhichao HAN',
      author_email='hanzhichao@gmail.com',
      packages=['pysentiment'],
      include_package_data=True,
      install_requires=['pandas >= 0.10',
                        'nltk >= 2.0'])
