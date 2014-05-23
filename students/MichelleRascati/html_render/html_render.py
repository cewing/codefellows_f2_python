#!/usr/bin/env python

"""
Python class example.

"""


# The start of it all:
# Fill it all in here.
class Element(object):
    tag = u"html"
    indent = u"  "

    def __init__(self, content=None):
        if content is not None:
            self.content = [content]
        else:
            self.content = []

    def append(self, text):
        """Add text string to content."""
        self.content.append(text)

    def render(self, file_out, ind=u""):
        """Render tag and string in conent.

        Keyword arguments:
        file_out -- File name in which to output render
        ind -- amount to indent tag (default "")
        """
        file_out.write(u'{}<{}>\n'.format(ind, self.tag))
        for item in self.content:
            try:
                item.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write(self.indent + ind + item + '\n')
        file_out.write(u'{}</{}>\n'.format(ind, self.tag))


class Html(Element):
    tag = u"html"


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"
