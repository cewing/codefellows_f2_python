#!/usr/bin/python
""" unit testing of html_render.py"""
import unittest
import html_render as hr
import cStringIO


def renderString(page):
    """ Returns string of rendered html"""
    f = cStringIO.StringIO()
    page.render(f)
    f.reset()
    return f.read()


class TestHtmlRender(unittest.TestCase):
    def test_Html(self):
        page = hr.Html()
        actual = renderString(page)
        expected = '<!DOCTYPE html>\n<html>\n</html>\n'

        self.assertEqual(expected, actual)

    def test_pAttribute(self):
        page = hr.Html()
        body = hr.Body()
        body.append(hr.P(u"Here is a paragraph of text.",
                    style=u"text-align: right; font-style: verdana;"))
        body.append(hr.P(u"And here is another piece of text."))
        page.append(body)
        actual = renderString(page)
        expected =\
            '<!DOCTYPE html>\n'\
            '<html>\n'\
            '    <body>\n'\
            '        <p style="text-align: right; font-style: verdana;">\n'\
            '            Here is a paragraph of text.\n'\
            '        </p>\n'\
            '        <p>\n'\
            '            And here is another piece of text.\n'\
            '        </p>\n'\
            '    </body>\n'\
            '</html>\n'

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()