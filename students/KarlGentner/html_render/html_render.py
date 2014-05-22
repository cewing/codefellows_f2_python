#!/usr/bin/python


class Element(object):
    tag = u""
    indent = "    "

    def __init__(self, content=None):
        if content is not None:
            self.content = [None]
        else:
            self.content = []

    def render(self, file_out, ind=""):

        file_out.write('\n<%s>\n' % self.tag)
        for item in self.content:
            try:
            #if its a Element obj, call its render method
            #if isinstance(item, Element):
                item.render(file_out, ind+self.indent)
            # if not, just write it
            # else:
            except AttributeError:
                file_out.write(self.indent+ind+item+'\n')
        file_out.write('\n</%s>' % self.tag)

    def append(self, a_string):
            self.content.append(a_string)


class Html(Element):
        tag = u"html"


class Body(Element):
        tag = u"body"


class P(Element):
        tag = u"p"