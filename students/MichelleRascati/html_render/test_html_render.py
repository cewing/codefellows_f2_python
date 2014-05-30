#!/usr/bin/env python
""" Test each class in html_render.py with py.test
"""
import codecs
import cStringIO
import pytest

import html_render as hr


def render(page):
    """
    render the tree of elements

    This uses cSstringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = cStringIO.StringIO()
    page.render(f)

    f.reset()

    return f.read()


def test_element():
    page = hr.Element()
    p1 = u"P1"
    page.append(p1)
    p2 = u"P2"
    page.append(p2)
    print render(page)
    assert render(page) == "<html>\n    {}\n    {}\n</html>".format(p1, p2)
