#!/usr/bin/env python

import codecs
import os
import re

from setuptools import setup

file_path = os.path.abspath(os.path.dirname(__file__))


def readfile(*parts):
    return codecs.open(os.path.join(file_path, *parts), 'r').read()


def find_version(*file_paths):
    version_file = readfile(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string')


setup(name='phrases',
      version=find_version('src', 'phrases', '__init__.py'),
      description='Print top 10, most common 3 word phrases in input',
      packages=['phrases'],
      package_dir={'': 'src'},
      scripts=['bin/phrases'],
      zip_safe=False)
