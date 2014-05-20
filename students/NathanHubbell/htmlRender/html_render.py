#!/usr/bin/env python
"""Python class example."""
import codecs, os, inspect
cwd=os.getcwd()

class Html(object):
    tag_name="html"
    indentation="    "

    def __init__(self,initContent=None):
        if initContent:
            self.content=[initContent]
        else:
            self.content=[]
    def append(self,input):
        self.content.append(input)

    def render(self,file_out, ind=""):
        file_out.write("<%s>\n%s%s"%(self.tag_name,self.indentation,ind))
        
        for element in self.content:
            if isinstance(element,(Body,P)):
                element.render(file_out)
            else:
                file_out.write("%s"%(element))
        
        file_out.write("\n</%s>"%(self.tag_name))

class Body(Html):
    tag_name="body"

class P(Body):
    tag_name="p"
