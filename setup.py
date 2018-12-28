# -*- coding: utf-8 -*-

"""
    @date: 12/24/18

"""

from setuptools import setup

required_packages = ['matplotlib', 'tk']

setup(name='GPPL',
      version='0.0.1',
      description='Graphical library based on matplot library',
#      long_description='<tbw>'

      author='ulix',
      author_email='ulisse.rubizzo@gmail.com',
      mantainer='ulix',

      platforms=['linux', 'BSD'],

      requires=required_packages,
      
      licence='GPLL',
      
)
