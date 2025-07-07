#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('./source/readme.md') as readme_file:
    readme = readme_file.read()

with open('./source/history.md') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Antoine Meheut",
    author_email='github.contacts@protonmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
    ],
    description="Funny prompts tool for playing with replicants",
    entry_points={
        'console_scripts': [
            'main=main.Deckard:main',
        ],
    },
    install_requires=requirements,
    license="MIT License",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='main',
    name='main',
    packages=find_packages(include=['main', 'main.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/AntoineMeheut/Deckard',
    version='0.1.0',
    zip_safe=False,
)
