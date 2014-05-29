import series
import pytest

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


def test_fibonacci():
    u"""
    Ensure the first 12 values returned by fibonacci() equal a known source.
    Also ensures the first 12 values returned by sum_series() with the
    default arguments matches the output.
    """
    for input_, output in fibonacci_vals:
        assert series.fibonacci(input_) == output
        assert series.sum_series(input_) == output


def test_lucas_vals():
    u"""
    Ensure the first 12 values returned by lucas() equal a known source.
    Also ensures the first 12 values returned by sum_series() called with
    iniital values equivalent to the first two values in lucas() matches the
    output.
    """
    for input_, output in lucas_vals:
        assert series.lucas(input_) == output
        assert series.sum_series(input_, 2, 1) == output


def test_bad_inputs():
    u"""
    Verify that fibonacci(), lucas(), and sum_series() catch all inputs that
    are not non-negative integers.
    """
    for badval in [3.14, 'a', []]:
        with pytest.raises(ValueError):
            fibonacci_result = series.fibonacci(badval)
            lucas_result = series.lucas(badval)
            sum_series_result = series.sum_series(badval)
