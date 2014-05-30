#!/usr/bin/env python

"""
code that tests the ack func defined in ack.py

can be run with py.test
"""

import pytest  # used for the exception testing
from ack import ack

def test_ack():
    ackFunc = [[1,2,3,4,5],[2,3,4,5,6],[3,5,7,9,11],[5,13,29,61,125]]

    for m in range(4):
        for n in range(5):
            assert ack(m,n) == ackFunc[m][n]

