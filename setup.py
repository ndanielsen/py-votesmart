import os
import re
import codecs

from setuptools import setup
from setuptools import find_packages

PROJECT = os.path.abspath(os.path.dirname(__file__))
REQUIRE_PATH = "requirements.txt"
EXCLUDES     = (
    "tests", "bin", "docs", "fixtures", "register", "notebooks", "examples",
)

long_description = open('README.rst').read()

def read(*parts):
    """
    Assume UTF-8 encoding and return the contents of the file located at the
    absolute path from the REPOSITORY joined with *parts.
    """
    with codecs.open(os.path.join(PROJECT, *parts), 'rb', 'utf-8') as f:
        return f.read()

def get_requires(path=REQUIRE_PATH):
    """
    Yields a generator of requirements as defined by the REQUIRE_PATH which
    should point to a requirements.txt output by `pip freeze`.
    """
    for line in read(path).splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            yield line

setup(name="py-votesmart",
      version="0.4.0aN",
      description="Libraries for interacting with the Project Vote Smart API",
      author="Nathan Danielsen <nathan.danielsen@gmail.com>",
      author_email = "nathan.danielsen@gmail.com",
      license="BSD",
      url="http://github.com/ndanielsen/py-votesmart/",
      long_description="py-votesmart is a fork of the original python-votesmart with python3 support",
      packages=find_packages(where=PROJECT, exclude=EXCLUDES),

      platforms=["any"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   'Programming Language :: Python',
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5"
                   ],
      install_requires=list(get_requires()),
      )
