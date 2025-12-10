#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst', 'r') as fh:
    long_description = fh.read()

# Read requirements from requirements.txt
with open('requirements.txt', 'r') as f:
    install_requires = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='social-analyzer',
    author='QeeqBox',
    author_email='gigaqeeq@gmail.com',
    description="API, CLI & Web App for analyzing & finding a person's profile across 300+ social media websites (Detections are updated regularly)",
    long_description=long_description,
    version='0.45',
    license='AGPL-3.0',
    url='https://github.com/qeeqbox/social-analyzer',
    py_modules=['app'],
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'social-analyzer=app:main',
        ],
    },
    python_requires='>=3.9',
)
