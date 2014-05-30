#!/usr/bin/env python
""" Test rot13 function in rot13.py with py.test
"""
import pytest

from rot13 import rot13

def test_rot13():
    assert rot13(u'The quick brown fox 123!?') == u'Gur dhvpx oebja sbk 123!?'
