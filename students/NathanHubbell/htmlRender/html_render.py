#!/usr/bin/env python
"""Python class example."""
import codecs, os, inspect
cwd=os.getcwd()



class Element(object):
    indentation="    "

    def __init__(self,initContent=None,**kwargs):
        if initContent:
            self.content=[initContent]
        else:
            self.content=[]
        #if kwargs:
        print kwargs
        self.kwargs=kwargs

    def append(self,input):
        self.content.append(input)

    def render(self,file_out, ind=""):
        file_out.write("%s<%s %s>\n"%(ind,self.kwargs,self.tag_name))
        for element in self.content:
            if isinstance(element,(Body,P,Head,Title)):
                element.render(file_out,ind + self.indentation) #consider using: element.render(file_out,ind + self.indentation)
            else:
                file_out.write("%s%s%s\n"%(ind,self.indentation,element))
        file_out.write("%s</%s>\n"%(ind,self.tag_name))

class Html(Element):
    tag_name="html"


class Body(Element):
    tag_name="body"

class P(Element):
    tag_name="p"

class Head(Element):
    tag_name="head"

class OneLineTag(Element):
    def render(self,file_out, ind=""):
        file_out.write("%s<%s> %s </%s>\n"%(ind,self.tag_name,self.content[0],self.tag_name))

class Title(OneLineTag):
    tag_name="title"

