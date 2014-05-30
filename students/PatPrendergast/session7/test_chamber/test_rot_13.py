#!usr/bin/env python

from rot_13 import rot_13

def test_string1():
    assert rot_13(u"ABC, abc, 123") == u'NOP, nop, 123'

def test_string2():
    assert rot_13(u'NOP, nop, 123') == u"ABC, abc, 123"

def test_string3():
    assert rot_13(u"Here is an EXAMPLE... Don't wear it out!") == "Urer vf na RKNZCYR... Qba'g jrne vg bhg!"

def test_empty():
    assert rot_13('') == ''

def test_punc():
    assert rot_13('!.,"$"') == '!.,"$"'