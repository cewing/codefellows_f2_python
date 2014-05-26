"""HTML Renderer Assignment"""

class Element(object):

    tag = ''
    indent = ""
    attr_str = ""

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            for k, v in kwargs.items():
                self.attr_str = self.attr_str + k + '=' + '"' + v + '" '

    def append(self, str):
        self.content.append(str)

    def render(self, file_out, ind=indent):
        if self.attr_str:
            file_out.write(self.indent + '<%s %s>\n' %(self.tag, self.attr_str))
        else:
            file_out.write(self.indent + '<%s>\n' %self.tag)
        for item in self.content:
            try:
                item.render(file_out, ind=self.indent)
            except AttributeError:
                file_out.write(self.indent + ind  + item + '\n')
        file_out.write(self.indent + '</%s>\n' %self.tag)

class Html(Element):
    tag = 'html'
    indent = ""

    def render(self, file_out, ind=indent):
        file_out.write("<!DOCTYPE html>\n")
        if self.attr_str:
            file_out.write(self.indent + '<%s %s>\n' %(self.tag, self.attr_str))
        else:
            file_out.write(self.indent + '<%s>\n' %self.tag)
        for item in self.content:
            try:
                item.render(file_out, ind=self.indent)
            except AttributeError:
                file_out.write(self.indent + ind  + item + '\n')
        file_out.write(self.indent + '</%s>\n' %self.tag)


class Body(Element):
    tag = 'body'
    indent = "    "

class P(Element):
    tag = 'p'
    indent = "        "

class Head(Element):
    tag = 'head'
    indent = "    "

class Title(Element):
    tag = 'title'
    indent = "        "

class Hr(Element):
    tag = 'hr'
    indent = "    "

    def render(self, file_out, ind=""):
        file_out.write(self.indent + '<%s /> \n' %self.tag)

class Br(Element):
    tag = 'br'
    indent = "    "

    def render(self, file_out, ind=""):
        file_out.write(self.indent + '<%s /> \n' %self.tag)

class A(Element):
    tag = 'a'
    attr_str = ""
    indent = ""

    def __init__(self, link, content):
        self.content = content
        self.kwargs = {u"href": link}
        super(A, self).__init__(self.content, **self.kwargs)

    def render(self, file_out, ind=""):
        file_out.write(self.indent + '<%s %s>' %(self.tag, self.attr_str))
        for item in self.content:
            try:
                item.render(file_out, ind="")
            except AttributeError:
                file_out.write(item)
        file_out.write(self.indent + '</%s> ' %self.tag)

class H(Element):
    tag = "h"
    indent = "        "

    def __init__(self, level, content):
        self.tag = self.tag + str(level)
        self.content = content
        super(H, self).__init__(self.content)

    def render(self, file_out, ind=indent):
        if self.attr_str:
            file_out.write(self.indent + '<%s %s>' %(self.tag, self.attr_str))
        else:
            file_out.write(self.indent + '<%s>' %self.tag)

        for item in self.content:
            try:
                item.render(file_out, ind=self.indent)
            except AttributeError:
                file_out.write(item)
        file_out.write('</%s>\n ' %self.tag)

class Ul(Element):
    tag = "ul"
    indent = "    "

class Li(Element):
    tag = "li"
    indent = "        "

class Meta(Element):
    tag = "meta"
    indent = ""

    def render(self, file_out, ind=indent):
        if self.attr_str:
            file_out.write(self.indent + '<%s %s>\n' %(self.tag, self.attr_str))
        else:
            file_out.write(self.indent + '<%s>\n' %self.tag)
        for item in self.content:
            try:
                item.render(file_out, ind=self.indent)
            except AttributeError:
                file_out.write(self.indent + ind  + item + '\n')