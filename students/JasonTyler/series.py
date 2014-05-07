"""For a code fellows assignment. A bunch of number series."""


def fibonacci(nth):
    """Return the nth value of the Fibonacci series, starting with index 1."""
    two_past = 0
    one_past = 1
    if not isinstance(nth, int) or nth < 1: return None
    elif nth == 1: return two_past
    elif nth == 2: return one_past
    else:
        for _ in range(nth - 2):
            next_ = one_past + two_past
            two_past = one_past
            one_past = next_
    return next_


def lucas(nth):
    """Return the nth value of the Lucas series, starting with index 1."""
    two_past = 2
    one_past = 1
    if not isinstance(nth, int) or nth < 1: return None
    elif nth == 1: return two_past
    elif nth == 2: return one_past
    else:
        for _ in range(nth - 2):
            next_ = one_past + two_past
            two_past = one_past
            one_past = next_
    return next_


def sum_series(nth, seed1=0, seed2=1):
    """
    Return nth value of sum_series using seed1 and seed2 as first two values.

    sum_series(nth, 0, 1) returns Fibonacci series. sum_series(nth, 2, 1) will
    return Lucas series.
    """
    two_past = seed1
    one_past = seed2
    if not isinstance(nth, int) or nth < 1: return None
    elif nth == 1: return two_past
    elif nth == 2: return one_past
    else:
        for _ in range(nth - 2):
            next_ = one_past + two_past
            two_past = one_past
            one_past = next_
    return next_

if __name__ == "__main__":
    """Test sequences against expected normal output and rubbish input."""

    fib_val = [
        [1, 0],
        [2, 1],
        [3, 1],
        [4, 2],
        [5, 3],
        [6, 5],
        [7, 8],
        [8, 13],
        [9, 21],
        [10, 34],
        [11, 55],
        [12, 89],
        [13, 144],
        [14, 233],
        [15, 377],
        [16, 610]
    ]

    fib_val_rubbish = [
        [0, None],
        [-10, None],
        [1.2, None],
        ["adsf", None]
    ]

    luc_val = [
        [1, 2],
        [2, 1],
        [3, 3],
        [4, 4],
        [5, 7],
        [6, 11],
        [7, 18],
        [8, 29],
        [9, 47],
        [10, 76],
        [11, 123]
    ]

    luc_val_rubbish = [
        [0, None],
        [-10, None],
        [1.2, None],
        ["adsf", None]
    ]

    # defining assertion functions
    def assert_fibonacci():
        """Assert test Fibonacci sequence using known vals and nonsense in."""
        for output_set in fib_val:
            assert fibonacci(output_set[0]) == output_set[1]
        for output_set in fib_val_rubbish:
            assert fibonacci(output_set[0]) == output_set[1]
        print "Fibonacci sequence tests ok."

    def assert_lucas():
        """Assert test Lucas sequence using known vals and nonsense input."""
        for output_set in luc_val:
            assert lucas(output_set[0]) == output_set[1]
        for output_set in luc_val_rubbish:
            assert lucas(output_set[0]) == output_set[1]
        print "Lucas sequence tests ok."

    def assert_sum_series():
        """Assert test sum_series"""

        # Testing using Fibonacci values
        for output_set in fib_val:
            assert sum_series(output_set[0]) == output_set[1]
        for output_set in fib_val_rubbish:
            assert sum_series(output_set[0]) == output_set[1]

        for output_set in luc_val:
            assert sum_series(output_set[0], 2, 1) == output_set[1]
        for output_set in luc_val_rubbish:
            assert sum_series(output_set[0], 2, 1) == output_set[1]
        print "Generalized sum_series sequence tests ok."

    # calling assertion funcitons
    assert_fibonacci()
    assert_lucas()
    assert_sum_series()
