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
            if isinstance(element,(Body,P,Head,Title)):
                file_out.write("%s"%(ind))
                element.render(file_out,"    ") #consider using: element.render(file_out,ind + self.indentation)
                file_out.write("%s"%(ind))
            else:
                file_out.write("%s%s%s\n%s%s"%(ind,ind,element,ind,ind))
        file_out.write("</%s>\n"%(self.tag_name))

class Body(Html):
    tag_name="body"

class P(Html):
    tag_name="p"

class Head(Html):
    tag_name="head"

class OneLineTag(Html):
   def render(self,file_out, ind=""):
       file_out.write("<%s> %s </%s>\n"%(self.tag_name,self.content,self.tag_name))

class Title(OneLineTag):
    tag_name="title"

