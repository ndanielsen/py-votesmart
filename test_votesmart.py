from __future__ import print_function

import doctest
doctest.testfile('README.rst', verbose=False, extraglobs={'print_function': print_function})
