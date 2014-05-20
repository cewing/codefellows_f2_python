#!/usr/bin/env python
"""Python class example."""
import codecs, os
cwd=os.getcwd()

class Html(object):
    tag_name="html"
    indentation="    "

    def __init__(self,initContent=None):
        self.content=[initContent]

    def append(self,text):
        self.content.append(text)

    def render(self,file_out, ind=""):
        file_out.write("<%s>\n%s%s%s\n</%s>"%(self.tag_name,self.indentation,ind,self.content,self.tag_name))

class Body(Html):
    pass

class P(Body):
    pass
