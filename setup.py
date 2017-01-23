#!/usr/bin/env python

import os
import re
import sys

from codecs import open

from distutils.core import setup
from distutils.cmd import Command

class PyTest(Command):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        self.pytest_args = []

    def finalize_options(self):
        self.test_args = []
        self.test_suite = True

    def run(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [ 'resaspy' ]

requires = []
test_requirements = []

with open('resaspy/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='resaspy',
    version=version,
    description='python for RESAS API.',
    long_description=readme,
    author='Masahiro Wada',
    author_email='argon.argon.argon@gmail.com',
    url='https://github.com/ar90n/resaspy',
    packages=packages,
    package_dir={'resaspy': 'resaspy'},
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Intended Audience :: Developers',
        'Natural Language :: Japanese',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
    install_requires=[
        'requests',
        'requests-cache',
    ],
)

