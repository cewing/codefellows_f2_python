
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

        file_out.write('\n%s<%s>\n' % (ind, self.tag) )
        for item in self.content:
            try:
            """you can check if the item is an instance of the element. it might be a string then .write will work. 
            or might be the element with tags
            if instance then item.render
            if string file_out.write

            """
                item.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write(self.indent+ind)
                file_out.write(item+'\n')
        file_out.write('<%s/%s>' % (ind, self.tag))
    def append(self, a_string):
        self.content.append(a_string)

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'