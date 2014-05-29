#!/usr/bin/env python

"""
code that tests the series module defined in series.py

can be run with py.test
"""

import pytest  # used for the exception testing
from series import fibonacci, lucas, sum_series


fibList = [None,0,1,1,2,3,5,8]
lucList = [None,2,1,3,4,7,11,18]

#Test the fibonacci function
def test_fib():
    for i in range(8):
        assert fibonacci(i-1)==fibList[i]

#test the lucas function
def test_luc():
    for i in range(8):
        assert lucas(i-1)==lucList[i]

#Test the  fibonacci sum_series function
def test_fib_sum():
    for i in range(8):
        assert sum_series(i-1)==fibList[i]

#test the lucas sum_series function
def test_luc_sum():
    for i in range(8):
        assert sum_series(i-1,2,1)==lucList[i]

