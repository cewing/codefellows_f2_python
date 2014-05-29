#!usr/bin/env python
''' Tests count evens module output values. '''

import pytest
import count_evens

def test_evens():
    assert count_evens.count_evens([0, 2, 4, 6, 8]) == 5

def test_mixed_up():
    assert count_evens.count_evens([2, 3, 9, 11, 4]) == 2

def test_empty_list():
    assert count_evens.count_evens([]) == 0

def test_check_weird():
    with pytest.raises(TypeError):
        assert count_evens.count_evens(['AAA', 'a'])
