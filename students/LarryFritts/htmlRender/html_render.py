"""HTML Renderer Assignment"""

class Element(object):

    tag = ''
    indent = ""
    attr_str = ""

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            for k, v in kwargs.items():
                self.attr_str = k + ' = ' + v

    def append(self, str):
        self.content.append(str)

    def render(self, file_out, ind=""):
        file_out.write(self.indent + '<%s %s> \n' %(self.tag, self.attr_str))
        for item in self.content:
            try:
                item.render(file_out, ind="    ")
            except AttributeError:
                file_out.write(self.indent + ind + item + '\n')
        file_out.write(self.indent + '<\%s>\n' %self.tag)

class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'



class P(Element):
    tag = 'p'
    indent = "    "



class Head(Element):
    tag = 'head'


class Title(Element):
    tag = 'title'
    indent = "    "


#class Hr(Element):
#    tag = 'hr'

