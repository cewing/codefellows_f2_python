import ack
import pytest

vals = {
    (0, 0): 1,
    (0, 1): 2,
    (0, 2): 3,
    (0, 3): 4,
    (0, 4): 5,
    (1, 0): 2,
    (1, 1): 3,
    (1, 2): 4,
    (1, 3): 5,
    (1, 4): 6,
    (2, 0): 3,
    (2, 1): 5,
    (2, 2): 7,
    (2, 3): 9,
    (2, 4): 11,
    (3, 0): 5,
    (3, 1): 13,
    (3, 2): 29,
    (3, 3): 61,
    (3, 4): 125,
    }  # Values from wikipedia.org/wiki/Ackermann_function

badvals = [
    ('a', 2.78),
    ('a', 'a'),
    ('a', []),
    (2.78, 2.78),
    (2.78, 'a'),
    (2.78, [])
    ]


def test_expected():
    u"""Assert that ack() reutrns expected values."""
    for input_ in vals:
        assert ack.ack(input_[0], input_[1]) == vals[input_]


def test_badvalues():
    u"""Verify that only positive integers are processed by the fucntion."""
    for badval in badvals:
        with pytest.raises(ValueError):
            result = ack.ack(badval[0], badval[1])
