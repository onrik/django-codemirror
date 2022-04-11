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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
