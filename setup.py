# -*- coding: utf-8 -*-

"""
    @date: 12/24/18

"""

from setuptools import setup, find_packages

required_packages = ['matplotlib', 'tk']

setup(name='GPPL',
      version='0.0.1',
      description='Graphical library based on matplot library',
#      long_description='<tbw>'

      author='ulix',
      author_email='ulisse.rubizzo@gmail.com',
      mantainer='ulix',

      packages=find_packages(),
      requires=required_packages,
      
      platforms=['linux', 'BSD'],
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
      ],
      license='GPLv3',
      
)
