#!/usr/bin/env python

"""
code that tests the rot13 method defined in rot13.py

can be run with py.test
"""

from rot13 import rot13


def test_rot13():
    upAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowAlpha = "abcdefghijklmnopqrstuvwxyz"
    upAlphaRot = upAlpha[13:] + upAlpha[:13]
    lowAlphaRot = lowAlpha[13:] + lowAlpha[:13]
    assert rot13(upAlpha) == upAlphaRot
    assert rot13(lowAlpha) == lowAlphaRot
    assert rot13("1234567890 !@#$%^&*()") == "1234567890 !@#$%^&*()"
