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

    This uses cSstringIO to render to memory, then returns
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
    assert render(page) == u"<html>\n    {}\n    {}\n</html>\n".format(p1, p2)


def test_html():
    page = hr.Html()
    assert render(page) == u"<!DOCTYPE html>\n<html>\n</html>\n"


def test_body():
    body = hr.Body()
    body.append("text")
    assert render(body) == u"<body>\n    text\n</body>\n"
