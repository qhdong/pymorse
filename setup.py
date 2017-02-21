# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(name='pymorse2',
      version='0.0.2',
      description="A python lib to translate unicode to morse code",
      long_description='',
      author='Dong Qihong',
      author_email='dongqihong@vip.qq.com',
      url='https://github.com/qhdong/pymorse',
      license='MIT',
      install_requires=[],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Topic :: Utilities'
      ],
      keywords='morse.py, pymorse, morse',
      packages=find_packages('src'),
      package_dir={'':'src'},
  )
