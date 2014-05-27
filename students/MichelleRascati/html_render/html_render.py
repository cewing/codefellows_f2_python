#!/usr/bin/env python

"""
Python class example.

"""


# The start of it all:
# Fill it all in here.
class Element(object):
    tag = u"html"
    indent = u"  "

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        self.attr = kwargs

    def append(self, text):
        """Add text string to content."""
        self.content.append(text)

    def render(self, file_out, ind=u""):
        """Render tag and string in conent.

        Keyword arguments:
        file_out -- File name in which to output render
        ind -- amount to indent tag (default "")
        """
        attr_str = u"".join([u' {}="{}"'.format(k, v) for k, v in
                            self.attr.items()])
        file_out.write(u'{}<{}{}>\n'.format(ind, self.tag, attr_str))
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


class Head(Element):
    tag = u"head"


class OneLineTag(Element):

    def render(self, file_out, ind=""):
        """Render a one line tag and string in conent.

        Keyword arguments:
        file_out -- File name in which to output render
        ind -- amount to indent tag (default "")
        """
        file_out.write(u'{}<{}>'.format(ind, self.tag))
        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(item)
        file_out.write(u'</{}>\n'.format(self.tag))


class Title(OneLineTag):
    tag = u"title"


class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        """Render a self closing tag and string in content.

        Keyword arguments:
        file_out -- File name in which to output render
        ind -- amount to indent tag (default "")
        """
        attr_str = u"".join([u' {}="{}"'.format(k, v) for k, v in
                            self.attr.items()])
        file_out.write(u'{}<{}{}'.format(ind, self.tag, attr_str))
        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(item)
        file_out.write(u' />\n'.format(self.tag))


class Hr(SelfClosingTag):
    tag = u"hr"


class Br(SelfClosingTag):
    tag = u"br"
