
#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.
class Element(object):
    tag = ''
    indent = "    "
    def __init__(self, content= None):
        if content is not None:
            self.content = [content]
        else:
            self.content = []
    def render(self, file_out, ind = ""):

        file_out.write('<%s>\n' % self.tag )
        for item in self.content:
            try:
                item.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(self.indent+ind)
                file_out.write(item+'\n')
        file_out.write('</%s>' % self.tag )
    def append(self, a_string):
        self.content.append(a_string)

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'