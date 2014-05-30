#!/usr/bin/env python

"""
code that tests the rot13 func defined in rot13.py

can be run with py.test
"""

import pytest  # used for the exception testing
from rot13 import rot13

def test_rot():
    assert rot13("hello friends") == "uryyb sevraqf"