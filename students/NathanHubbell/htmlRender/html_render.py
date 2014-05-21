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
        file_out.write("<%s>\n%s"%(self.tag_name,self.indentation))
        
        for element in self.content:
            if isinstance(element,(Body,P)):
                file_out.write("%s"%(ind))
                element.render(file_out,"    ")
                file_out.write("%s"%(ind))
            else:
                file_out.write("%s%s%s\n%s%s"%(ind,ind,element,ind,ind))
        
        file_out.write("</%s>\n"%(self.tag_name))

class Body(Html):
    tag_name="body"

class P(Body):
    tag_name="p"
