def fibonacci(n):

    """
    Return the nth integer in the Fibonacci series.

    Argument:
    n: A positive integer.

    Return value: A positive integer.
    """

    def check_value(n):
        if not isinstance(n, int):
            raise ValueError
        if n < 0:
            return None
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

    """
    Return the nth integer in the Lucas series.

    Argument:
    n: A nonnegative integer.

    Return value: A positive integer.
    """

    def check_value(n):
        if not isinstance(n, int):
            raise ValueError
        if n < 0:
            return None
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


def sum_series(n, n0=0, n1=1):

    """
    Return the nth int in an summed int sequence started by given args.

    Arguments:
    n: A nonnegative integer.
    n0: A nonnegative integer.
    n1: A nonnegative integer.

    Return value: A positive integer.
    """

    def check_value(n):
        if not isinstance(n, int):
            raise ValueError
        if n < 0:
            return None
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

# if __name__ == "__main__":
#     fibonacci_vals = [
#         (0, 0),
#         (1, 1),
#         (2, 1),
#         (3, 2),
#         (4, 3),
#         (5, 5),
#         (6, 8),
#         (7, 13),
#         (8, 21),
#         (9, 34),
#         (10, 55),
#         (11, 89),
#         (12, 144)
#         ]  # Values from http://en.wikipedia.org/wiki/Fibonacci_number
#     lucas_vals = [
#         (0, 2),
#         (1, 1),
#         (2, 3),
#         (3, 4),
#         (4, 7),
#         (5, 11),
#         (6, 18),
#         (7, 29),
#         (8, 47),
#         (9, 76),
#         (10, 123),
#         (11, 199),
#         (12, 322)
#         ]  # Values from http://oeis.org/A000204

#     # Ensure the first 12 values returned by fibonacci() equal a known source.
#     # Also ensures the first 12 values returned by sum_series() with the
#     # default arguments matches the output
#     for input_, output in fibonacci_vals:
#         assert fibonacci(input_) == output
#         assert sum_series(input_) == output

#     # Ensure the first 12 values returned by lucas() equal a known source.
#     # Also ensures the first 12 values returned by sum_series() called with
#     # iniital values equivalent to the first two values in lucas() matches the
#     # output.
#     for input_, output in lucas_vals:
#         assert lucas(input_) == output
#         assert sum_series(input_, 2, 1) == output

#     # Verify that fibonacci(), lucas(), and sum_series() catch all inputs that
#     # are not non-negative integers
#     for badval in [3.14, 'a', []]:
#         try:
#             fibonacci_result = fibonacci(badval)
#             lucas_result = lucas(badval)
#             sum_series_result = sum_series(badval)
#         except ValueError:
#             pass
#         else:
#             print u"A bad value did not trigger a ValueError!"
#             assert(False)

#     print u"All tests passed!"