
#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.
class Element(object):
    tag = ''
    indent = "    "
    def __init__(self, content= None, **kwargs):
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        
        self.attributes = kwargs

    def render(self, file_out, ind = ""):
        attributes = ''
        for (k,v) in self.attributes.items():
            attributes += (' {key} = "{value}"'.format(key = k, value = v))
        file_out.write('\n%s<%s%s>\n' % (ind, self.tag, attributes))
        for item in self.content:
            try:
                item.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(self.indent+ind)
                file_out.write(item)
        file_out.write('\n%s</%s>' % (ind, self.tag))
    def append(self, a_string):
        self.content.append(a_string)

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'
class Head(Element):
    tag = 'head'
class Title(Element):
    tag = 'title'
    def render(self, file_out, ind = ""):

        file_out.write('\n%s<%s>' % (ind, self.tag) )
        for item in self.content:
            try:

                item.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(self.indent+ind)
                file_out.write(item)
        file_out.write('%s</%s>' % (ind, self.tag))
class SelfClosingTag(Element):
    def render(self, file_out, ind = ""):
        attributes = ''
        for (k,v) in self.attributes.items():
            attributes += ' {key} = "{value}"'.format(key = k, value = v)
        file_out.write('\n%s<%s%s />\n' % (ind, self.tag, attributes))
class Hr(SelfClosingTag):
    tag = 'hr'
class Br(SelfClosingTag):
    tag = 'br'
class A(Element):
    tag = 'a'
    def __init__(self, link = None, content=None):
        link = dict(href = link)
        Element.__init__(self, content, **link)
        



    


"""you can check if the item is an instance of the element. it might be a string then .write will work. 
or might be the element with tags
if instance then item.render
if string file_out.write
"""    