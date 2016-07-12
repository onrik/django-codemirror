#!/usr/bin/env python

from setuptools import setup, find_packages
from codemirror import __version__

setup(
    name='django-codemirror',
    version=__version__,
    author='Andrey',
    author_email='and@rey.im',
    url='https://github.com/onrik/django-codemirror',
    description='Django codemirror widget',
    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
