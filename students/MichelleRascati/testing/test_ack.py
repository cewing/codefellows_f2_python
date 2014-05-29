#!/usr/bin/env python
""" Test ack function in ack.py with py.test
"""
import pytest

from ack import ack

def test_ack():
    result = [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 5, 7, 9, 11, 5, 13, 29, 61, 125]
    result.reverse()
    vals = []

    for i in range(4):
        for j in range(5):
            vals.append([i,j,result.pop()])

    for val in vals:
        assert ack(val[0], val[1]) == val[2]