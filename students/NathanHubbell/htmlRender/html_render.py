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
        file_out.write("%s<%s>\n"%(ind,self.tag_name))
        for element in self.content:
            if isinstance(element,(Body,P,Head,Title)):
                element.render(file_out,ind + self.indentation) #consider using: element.render(file_out,ind + self.indentation)
            else:
                file_out.write("%s%s%s\n"%(ind,self.indentation,element))
        file_out.write("%s</%s>\n"%(ind,self.tag_name))

class Body(Html):
    tag_name="body"

class P(Html):
    tag_name="p"

class Head(Html):
    tag_name="head"

class OneLineTag(Html):
    def render(self,file_out, ind=""):
        file_out.write("%s<%s> %s </%s>\n"%(ind,self.tag_name,self.content[0],self.tag_name))

class Title(OneLineTag):
    tag_name="title"

