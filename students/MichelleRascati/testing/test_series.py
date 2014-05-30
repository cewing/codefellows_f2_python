#!/usr/bin/env python
""" Test each function in series.py with py.test
"""
import pytest

from series import *

fib = [0, 1, 1, 2, 3, 5, 8, 13]
luc = [2, 1, 3, 4, 7, 11, 18, 29]

def test_fibonacci():
    for i, val in enumerate(fib, start=1):
        assert val == fibonacci(i)

def test_lucas():
    for i, val in enumerate(luc, start=1):
        assert val == lucas(i)

def test_sum_series():
    for i, val in enumerate(fib, start=1):
        assert val == sum_series(i)
    for i, val in enumerate(luc, start=1):
        assert val == sum_series(i, 2, 1)