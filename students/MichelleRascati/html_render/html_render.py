#!/usr/bin/env python

"""
Python class example.

"""


# The start of it all:
# Fill it all in here.
class Element(object):
    tag = u"html"
    indent = u"    "

    def __init__(self, content=None):
        if content is not None:
            self.content = [content]
        else:
            self.content = []

    def append(self, text):
        """Add text string to content."""
        self.content.append(text)

    def render(self, file_out, ind=u""):
        """Render tag and string in conent."""
        file_out.write(u'<{}>\n'.format(self.tag))
        for item in self.content:
            file_out.write(self.indent + ind + item + '\n')
        file_out.write(u'</{}>\n'.format(self.tag))
