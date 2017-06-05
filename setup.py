#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['numpy']

test_requirements = []

setup(
    author='Stefan Fischer',
    author_email='sfischer13@ymail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
    description='Python implementations of common string distance and similarity algorithms.',
    include_package_data=True,
    install_requires=requirements,
    keywords='string metric distance similarity phonetic hamming levenshtein',
    license='MIT',
    long_description=readme + '\n\n' + history,
    name='stringmetric',
    package_dir={'stringmetric': 'stringmetric'},
    packages=['stringmetric'],
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sfischer13/python-stringmetric',
    version='0.2.0',
    zip_safe=False
)
