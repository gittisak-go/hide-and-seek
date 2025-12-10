#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='social-analyzer',
    author='QeeqBox',
    author_email='gigaqeeq@gmail.com',
    description="API, CLI & Web App for analyzing & finding a person's profile across 300+ social media websites (Detections are updated regularly)",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    version='0.45',
    license='AGPL-3.0',
    url='https://github.com/qeeqbox/social-analyzer',
    packages=find_packages(exclude=['tests', 'test', 'docs']),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'social-analyzer=app:main',
        ],
    },
    install_requires=[
        'beautifulsoup4>=4.9.0,<5.0.0',
        'tld>=0.12.0,<1.0.0',
        'termcolor>=1.1.0,<3.0.0',
        'langdetect>=1.0.9,<2.0.0',
        'requests>=2.25.0,<3.0.0',
        'lxml>=4.6.0,<5.0.0',
        'galeodes>=0.0.1,<1.0.0',
        'urllib3>=1.26.0,<3.0.0',
    ],
    package_data={
        '': ['data/*'],
    },
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
