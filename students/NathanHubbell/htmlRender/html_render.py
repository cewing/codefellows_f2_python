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
        self.kwargs=kwargs

    def append(self,input):
        self.content.append(input)

    def render(self,file_out, ind=""):
        if self.kwargs != {}:
            file_out.write("%s<%s "%(ind,self.tag_name))
            commaCount=0
            for key in self.kwargs:
                if commaCount<1:
                    file_out.write("%s=\"%s\""%(key,self.kwargs[key]))
                else:
                    file_out.write(", %s=\"%s\""%(key,self.kwargs[key]))
            file_out.write(">\n")
        else:
            file_out.write("%s<%s>\n"%(ind,self.tag_name))
        for element in self.content:
            if isinstance(element,(Body,P,Head,Title,Hr,Br,A,H,Ul,Li)):
                element.render(file_out,ind + self.indentation) #consider using: element.render(file_out,ind + self.indentation)
            else:
                file_out.write("%s%s%s\n"%(ind,self.indentation,element))
        file_out.write("%s</%s>\n"%(ind,self.tag_name))

class OneLineTag(Element):
    def render(self,file_out, ind=""):
        file_out.write("%s<%s> %s </%s>\n"%(ind,self.tag_name,self.content[0],self.tag_name))

class SelfClosingTag(Element):
    def render(self,file_out, ind=""):
        if self.content:
            file_out.write("%s<%s %s/>\n"%(ind,self.tag_name,self.content[0]))
        else:
            file_out.write("%s<%s />\n"%(ind,self.tag_name))
class A(SelfClosingTag):
    tag_name="href"
    def __init__(self, link, content):
        self.link = link
        if content:
            self.content=[content]
        else:
            self.content=[]

class Html(Element):
    tag_name="html"

class Body(Element):
    tag_name="body"

class P(Element):
    tag_name="p"

class Head(Element):
    tag_name="head"

class Ul(Element):
    tag_name="ul"

class Li(Element):
    tag_name="li"

class Title(OneLineTag):
    tag_name="title"

class Hr(SelfClosingTag):
    tag_name="hr"

class Br(SelfClosingTag):
    tag_name="br"

class H(OneLineTag):
    tag_name="h"
    def __init__(self,num,content):
        H.tag_name = "h" + str(num)
        self.content = [content]



