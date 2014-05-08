#!/usr/bin/env python

def sum_series(n, i = 0, j = 1):
    u"""Return the nth value of a number series consecutively adding i to j"""
    u"""Default parameters result in the Fibonacci series"""

    if n < 1:
        return None
    elif n == 1:
        return i
    elif n == 2:
        return j
    else:
        return sum_series(n - 1, j, i + j)


def fibonacci(n):
    u"""Return the nth value in the Fibonacci series"""

    return sum_series(n)


def lucas(n):
    u"""Return the nth value in the Lucas Numbers"""

    return sum_series(n, 2, 1)


if __name__ == '__main__':
    print u"Testing numerical series functions"

    print u"\nTesting fibonacci series function"
    # fib_tests values: n, expected result
    fib_tests = ((-1, None),
                 (0, None),
                 (1, 0),
                 (2, 1),
                 (3, 1),
                 (4, 2),
                 (5, 3),
                 (6, 5),
                 (7, 8),
                 (8, 13))

    for n, expected in fib_tests:
        print u"assert fibonacci(", n, ") == ", expected
        assert fibonacci(n) == expected


    print u"\nTesting Lucas numbers function"
    # lucas_tests values: n, expected result
    lucas_tests = ((-1, None),
                   (0, None),
                   (1, 2),
                   (2, 1),
                   (3, 3),
                   (4, 4),
                   (5, 7),
                   (6, 11),
                   (7, 18),
                   (8, 29))

    for n, expected in lucas_tests:
        print u"assert lucas(", n, ") == ", expected
        assert lucas(n) == expected

    print u"\nTesting sum_series function"
    # sum_series_tests values: n, expected result
    sum_series_tests = ((-1, 0, 1, None),
                        (0, 2, 1, None),
                        (1, 0, 1, 0),
                        (2, 0, 1, 1),
                        (3, 0, 1, 1),
                        (4, 0, 1, 2),
                        (5, 2, 1, 7),
                        (6, 2, 1, 11),
                        (7, 2, 1, 18),
                        (8, 2, 1, 29))

    for n, i, j, expected in sum_series_tests:
        print u"assert sum_series(", n, ", i, ", i, " j, ", j, ") == ", 
        print expected
        assert sum_series(n, i, j) == expected

    print u"\nAll tests pass"


