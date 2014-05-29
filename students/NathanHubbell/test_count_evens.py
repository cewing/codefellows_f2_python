#!/usr/bin/env python

"""
code that tests the count_evens function defined in count_evens.py

can be run with py.test
"""

import pytest  # used for the exception testing
import count_evens

def test_evens():
    a=count_evens.count_evens([1,2,4,6,7,8])
    assert a==[2,4,6,8]
