#!/usr/bin/python
""" classes and subclasses for rendering html with indentation"""

class Element(object):
    tag = u""
    attributes = u""
    link = u""

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            for key, value in kwargs.iteritems():
                self.attributes += ' ' + key + '="' + value + '"'

    def render(self, file_out, indent=u""):
        file_out.write(indent+u'<%s%s%s>\n' % (self.tag, self.attributes, self.link))
        closeIndent = indent
        indent += u"    "
        for item in self.content:
            try:
                # if its a Element obj, call its render method
                item.render(file_out, indent)
            # if not, just write it
            except AttributeError:
                file_out.write(indent+item + u'\n')
        file_out.write(closeIndent + u'</%s>\n' % self.tag)

    def append(self, a_string):
            self.content.append(a_string)


class OneLineTag(Element):
    def render(self, file_out, indent=u""):
        file_out.write(indent+u'<%s%s%s>' % (self.tag, self.attributes, self.link))
        indent += u"    "
        for item in self.content:
            try:
                item.render(file_out, indent)
            except AttributeError:
                file_out.write(item)
        file_out.write(u'</%s>\n' % self.tag)


class SelfClosingTag(Element):
    def render(self, file_out, indent=u""):
        file_out.write(indent+u'<%s%s%s' % (self.tag, self.attributes, self.link))
        indent += u"    "
        for item in self.content:
            try:
                item.render(file_out, indent)
            except AttributeError:
                file_out.write(indent+item)
        file_out.write(u' />\n')


# html
class Html(Element):
    tag = u"html"

    def render(self, file_out, indent=u""):
        file_out.write(u'<!DOCTYPE html>\n'+indent+u'<%s%s%s>\n' % (self.tag, self.attributes, self.link))
        closeIndent = indent
        indent += u"    "
        for item in self.content:
            try:
                item.render(file_out, indent)
            except AttributeError:
                file_out.write(indent+item + u'\n')
        file_out.write(closeIndent+u'</%s>\n' % self.tag)


# body
class Body(Element):
    tag = u"body"


# paragraph
class P(Element):
    tag = u"p"


# head
class Head(Element):
    tag = u"head"


# title
class Title(OneLineTag):
    tag = u"title"


# meta
class Meta(SelfClosingTag):
    tag = u"meta"


# horizontal rule
class Hr(SelfClosingTag):
    tag = u"hr"


# line break
class Br(SelfClosingTag):
    tag = u"br"


# anchor
class A(OneLineTag):
    tag = u"a"

    def __init__(self, link=None, content=None):
        if link is not None:
            self.link = ' href="' + link+'"'
        Element.__init__(self, content)


# unorcered list
class Ul(Element):
    tag = u"ul"


# ordered list
class Ol(Element):
    tag = u"ol"


# list item
class Li(Element):
    tag = u"li"


# heading
class H(OneLineTag):
    tag = u"h"

    def __init__(self, size=None, content=None):
        if size is not None:
            self.tag = (u"h%s" % str(size))
        Element.__init__(self, content)

##########################################################
