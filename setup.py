#!/usr/bin/env python

from distutils.core import setup
from codemirror import __version__

setup(
    name='django-codemirror',
    version=__version__,
    author='Andrey',
    author_email='and@rey.im',
    url='https://github.com/onrik/django-codemirror',
    description='Django form widget for CodeMirror text editor',
    packages=['codemirror'],
    package_data={'codemirror': [
        'static/css/*.css',
        'static/js/*.js'
    ]},
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
