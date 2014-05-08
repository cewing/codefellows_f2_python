#!/usr/bin/env python

def sum_series(n, i = 0, j = 1):
    u"""Return the nth value of a number series consecutively adding i to j"""
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
    print u"Testing numerical series functions\n"

    print u"Testing fibonacci series function"
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


    print u"Testing Lucas numbers function\n"
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

    print u"All tests pass"


