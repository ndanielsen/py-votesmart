.. image:: https://travis-ci.org/ndanielsen/py-votesmart.svg?branch=develop
    :target: https://travis-ci.org/ndanielsen/py-votesmart
.. image:: https://coveralls.io/repos/github/ndanielsen/py-votesmart/badge.svg?branch=develop
    :target: https://coveralls.io/github/ndanielsen/py-votesmart?branch=develop

================
py-votesmart
================

Python 3 supported library for interacting with the Project Vote Smart API.

The Project Vote Smart API provides detailed information on politicians,
including bios, votes, and NPAT responses.
(http://votesmart.org/services_api.php)

All code is under a BSD-style license, see LICENSE for details.

================
Backstory
================
py-votesmart is a fork of the python-votesmart which is a project of Sunlight Labs (c) 2008.
Originally written by James Turk <jturk@sunlightfoundation.com>.

Original Source: https://github.com/votesmart/python-votesmart

Installation
============
py-votesmart is compatible with Python 2.7 or later, but it is preferred to use Python 3.5 or later to take full advantage of all functionality. The simplest way to install py-votesmart is from PyPI with pip, Python’s preferred package installer.

    >>> pip install py-votesmart

Usage
=====

To initialize the api, all that is required is for it to be imported and for an
API key to be defined.

(If you do not have an API key visit http://votesmart.org/services_api.php to
register for one.)

Import ``votesmart`` from ``VoteSmartAPI``:

    >>> from votesmart import VoteSmartAPI

And set your API key:

    >>> vsmart = VoteSmartAPI(api_key="VOTE_SMART_API_KEY")


More documented use to come.
