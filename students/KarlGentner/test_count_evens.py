#!/usr/bin/env python

"""
code that tests the count_evens method defined in count_evens.py

can be run with py.test
"""

import pytest
from count_evens import count_evens


def test_evens():
    l = [-7.22, -6.10, -5.00, -4.00, -3.0, -2.0, -1, 0, 1, 2, 3, 4, 5, 6, 7]
    assert count_evens(l) == 6

    with pytest.raises(TypeError):
        l = ['0', '1', '2', 3, 4]
        assert count_evens(l) == 1