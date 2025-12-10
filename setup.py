#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r', encoding='utf-8') as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith('#')]

setup(
    name='social-analyzer',
    version='0.45',
    author='QeeqBox',
    author_email='gigaqeeq@gmail.com',
    description="API, CLI & Web App for analyzing & finding a person's profile across 300+ social media websites (Detections are updated regularly)",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license='AGPL-3.0',
    url='https://github.com/qeeqbox/social-analyzer',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'social_analyzer': ['data/*'],
    },
    install_requires=requirements,
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'social-analyzer=social_analyzer.app:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
