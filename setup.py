#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-facebook-utils',
    version='1.0',
    description='Some Facebook utilities to use in Django projects',
    author='Caio Ariede',
    author_email='caio.ariede@gmail.com',
    long_description=open('README.md', 'r').read(),
    url='http://github.com/caioariede/django-facebook-utils/',
    packages=[
        'facebook_utils',
        'facebook_utils.management',
        'facebook_utils.management.commands',
    ],
    install_requires=[
        'requests>=1.1.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
