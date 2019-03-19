#!/usr/bin/env python3

from setuptools import setup

import ctmd5

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='ctmd5',
    version=ctmd5.__VERSION__,
    description='change the MD5',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    author='shkey',
    author_email='shkey325@gmail.com',
    python_requires='>=3',
    url='https://github.com/shkey/change-the-md5',
    keywords='MD5',
    py_modules=['ctmd5'],
    entry_points={
        'console_scripts': ['ctmd5=ctmd5:cli'],
    },
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
