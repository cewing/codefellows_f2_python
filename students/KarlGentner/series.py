def fibonacci(n):
    """Return n-th value of the Fibonacci series"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return n-th value of the Lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, x=0, y=1):
    """Return n-th value of sum series with optional base case parameters"""
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)


# testing
if __name__ == '__main__':
    # Fibonacci list of paired inputs and expected outputs.
    fiboInOut = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8),
                 (7, 13), (8, 21), (9, 34), (10, 56)]
    # Lucas list of paired inputs and expected outputs.
    lucasInOut = [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18),
                  (7, 29), (8, 47), (9, 76), (10, 123)]
    # Checking actual results with expected results from fiboInOut list
    for n, result in fiboInOut:
        assert fibonacci(n) == result
        assert sum_series(n) == result
    # Checking actual results with expected results from lucasInOut list
    for n, result in lucasInOut:
        assert lucas(n) == result
        assert sum_series(n, 2, 1) == result
    print "All Tests Passed"
