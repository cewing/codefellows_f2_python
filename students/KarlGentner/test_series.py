#!/usr/bin/env python

"""
code that tests the ack method defined in ack.py

can be run with py.test
"""

from series import fibonacci, lucas, sum_series


def test_fibo_and_sumseries():
    # Fibonacci list of paired inputs and expected outputs.
    fiboInOut = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8),
                 (7, 13), (8, 21), (9, 34), (10, 55)]
    # Checking actual results with expected results from fiboInOut list
    for n, result in fiboInOut:
        assert fibonacci(n) == result
        assert sum_series(n) == result


def test_lucas_and_sumseries():
    # Lucas list of paired inputs and expected outputs.
    lucasInOut = [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18),
                  (7, 29), (8, 47), (9, 76), (10, 123)]

    # Checking actual results with expected results from lucasInOut list
    for n, result in lucasInOut:
        assert lucas(n) == result
        assert sum_series(n, 2, 1) == result
