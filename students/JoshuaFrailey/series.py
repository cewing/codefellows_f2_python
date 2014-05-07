def fibonacci(n):
    """Return the nth value in the Fibonacci series.

    Arguments:
    n: A positive integer.
    Return value: A positive integer.
    """

    def check_value(n):
        if not isinstance(n, int):
            raise ValueError
        if n < 0:
            raise ValueError
        return True

    def recursive_fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return recursive_fib(n-1) + recursive_fib(n-2)

    if check_value(n):
        return recursive_fib(n)


def lucas(n):
    """Return the nth value in the Lucas series.

    Arguments:
    n: A nonnegative, nonzero integer.
    Return value: A positive integer.
    """

    def check_value(n):
        if not isinstance(n, int):
            raise ValueError
        if n < 0:
            raise ValueError
        return True

    def recursive_lucas(n):
            if n == 0:
                return 2
            elif n == 1:
                return 1
            else:
                return recursive_lucas(n-1) + recursive_lucas(n-2)

    if check_value(n):
        return recursive_lucas(n)


def series_sum(n, n0=0, n1=1):
    """Return the nth value in a.
    """
    def check_value(n):
        if not isinstance(n, int):
            raise ValueError
        if n < 0:
            raise ValueError
        return True

    def rercursive_sum(n, n0, n1):
        if n == 0:
            return n0
        elif n == n1:
            return n1
        else:
            return rercursive_sum(n-1, n0, n1) + rercursive_sum(n-2, n0, n1)

    if check_value(n):
        return rercursive_sum(n, n0, n1)

if __name__ == "__main__":
    fibonacci_vals = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144)
        ]  # Values from http://en.wikipedia.org/wiki/Fibonacci_number
    lucas_vals = [
        (0, 2),
        (1, 1),
        (2, 3),
        (3, 4),
        (4, 7),
        (5, 11),
        (6, 18),
        (7, 29),
        (8, 47),
        (9, 76),
        (10, 123),
        (11, 199),
        (12, 322)
        ]  # Values from http://oeis.org/A000204

    for input_, output in fibonacci_vals:
        assert fibonacci(input_) == output

    for input_, output in lucas_vals:
        assert lucas(input_) == output

    for badval in [1, -2.78, 3.14, 'a', []]:
        try:
            fibonacci_result = fibonacci(badval)
            lucas_result = lucas(badval)
            # sum_series_result = sum_series(badval)
        except ValueError:
            pass
        else:
            print u"A bad value did not trigger a ValueError in fibonacci()!"

    # for badval in [-1, -2.78, 3.14, 'a', []]:
    #     try:
    #         lucas_result = lucas(badval)
    #         # lucas_result = lucas(badval)
    #         # sum_series_result = sum_series(badval)
    #     except ValueError:
    #         pass
    #     else:
    #         print u"A bad value did not trigger a ValueError in lucas()!"

    print u"All tests passed!"