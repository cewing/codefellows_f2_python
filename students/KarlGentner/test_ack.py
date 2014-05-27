#!/usr/bin/env python

"""
code that tests the ack method defined in ack.py

can be run with py.test
"""

from ack import ack


def test_ack():
    ackTable = ((1, 2, 3, 4), (2, 3, 4, 5), (3, 5, 7, 9), (5, 13, 29, 61))
    for i, x in enumerate(ackTable):
        for j, y in enumerate(x):
            assert ack(i, j) == y