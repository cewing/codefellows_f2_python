#!/usr/bin/python


class Element(object):
    tag = u""
    indent = u""
    attributes = u""
    link = u""

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            for key, value in kwargs.iteritems():
                self.attributes += ' ' + key + '="' + value + '" '

    def render(self, file_out, ind=u"    "):
        file_out.write(self.indent+u'<%s%s%s>\n' % (self.tag, self.attributes, self.link))
        for item in self.content:
            try:
                # if its a Element obj, call its render method
                item.render(file_out, self.indent + ind)
            # if not, just write it
            except AttributeError:
                file_out.write(self.indent+ind+item + u'\n')
        file_out.write(self.indent+u'</%s>\n' % self.tag)

    def append(self, a_string):
            self.content.append(a_string)


class OneLineTag(Element):
    indent = u""

    def render(self, file_out, ind=u"    "):
        file_out.write(self.indent+u'<%s%s%s>' % (self.tag, self.attributes, self.link))
        for item in self.content:
            try:
                item.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write(item)
        file_out.write(u'</%s>\n' % self.tag)


class SelfClosingTag(Element):
    def render(self, file_out, ind=u"    "):
        file_out.write(self.indent+u'<%s%s%s' % (self.tag, self.attributes, self.link))
        for item in self.content:
            try:
                item.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write(self.indent+ind+item)
        file_out.write(u' />\n')


# html
class Html(Element):
    tag = u"html"

    def render(self, file_out, ind=u"    "):
        file_out.write(u'<!DOCTYPE html>\n'+self.indent+u'<%s%s%s>\n' % (self.tag, self.attributes, self.link))
        for item in self.content:
            try:
                item.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write(self.indent+ind+item + u'\n')
        file_out.write(self.indent+u'</%s>\n' % self.tag)


# body
class Body(Element):
    tag = u"body"


# paragraph
class P(Element):
    tag = u"p"
    indent = u"    "


# head
class Head(Element):
    tag = u"head"


# title
class Title(OneLineTag):
    tag = u"title"
    indent = u"    "


# meta
class Meta(SelfClosingTag):
    tag = u"meta"
    indent = u"    "


# horizontal rule
class Hr(SelfClosingTag):
    tag = u"hr"
    indent = u"    "


# line break
class Br(SelfClosingTag):
    tag = u"br"
    indent = u"    "


# anchor
class A(OneLineTag):
    tag = u"a"
    indent = u"    "

    def __init__(self, link=None, content=None):
        if link is not None:
            self.link = ' href="' + link+'"'
        Element.__init__(self, content)


# unorcered list
class Ul(Element):
    tag = u"ul"
    indent = u"    "


# ordered list
class Ol(Element):
    tag = u"ol"
    indent = u"    "


# list item
class Li(Element):
    tag = u"li"
    indent = u"        "


# heading
class H(OneLineTag):
    tag = u"h"
    indent = u"    "

    def __init__(self, size=None, content=None):
        if size is not None:
            self.tag = (u"h%s" % str(size))
        Element.__init__(self, content)