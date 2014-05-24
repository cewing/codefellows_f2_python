#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.
class Element(object):
    ''' Describe the Html render class'''
    
    tag = ''
    indent = '    '
    #html_attributes dict?

    def __init__(self, content=None):
        if content is not None:
            self.content = [content]
        else:
            self.content = []

    def render(self, file_out, ind='', **html_attributes):
        
        file_out.write('\n%s<%s %s=%s>' % (ind, self.tag, (i for i in html_attributes.items()))
        for item in self.content:
            try:
                item.render(file_out, ind+self.indent)
            except AttributeError:
                file_out.write('\n' + self.indent + ind + item)
        file_out.write('\n%s<%s/> ' % (ind, self.tag))

    def append(self, a_string):
        self.content.append(a_string)

class Html(Element):
    tag = u'html'


class Body(Element):
    tag = u'body'

class P(Element):
    tag = u'p'

class Head(Element):
    tag = u'head'


class OneLineTag(Element):
    ''' Renders a one line tage where appropriate from the Element class '''
    def render(self, file_out, ind=''):
        file_out.write('\n%s<%s>' % (ind, self.tag))
        for item in self.content:
            try:
                item.render(file_out, ind+self.indent)
            except AttributeError:
                file_out.write(item)
        file_out.write('<%s/> ' % (self.tag))

class Title(OneLineTag):
    tag = u'title'
        

class SelfClosingTag(Element):
    ''' Renders a one line tage where appropriate from the Element class '''
    def render(self, file_out, ind=''):
        file_out.write('\n%s<%s ' % (ind, self.tag))
        for item in self.content:
            try:
                item.render(file_out, ind+self.indent)
            except AttributeError:
                file_out.write(item)
        file_out.write('/> ')

class Hr(SelfClosingTag):
    tag = u'hr/'

class Br(SelfClosingTag):
    tag = u'br/'

class A(SelfClosingTag):
    pass
