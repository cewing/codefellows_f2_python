

class Element(object):

    tag = ''
    indent = "    "

    def __init__(self, content=None):
        if content is not None:
            self.content = [content]
        else:
            self.content = []

    def append(self, str):
        """Do I need the try?"""
        try:
           self.content.append(str)
        except TypeError:
            pass

    def render(self, file_out, ind=""):
        file_out.write('<%s> \n' %self.tag)
        for item in self.content:
            try:
                item.render(file_out, ind="")
            except AttributeError:
                file_out.write(self.indent + ind + item + '\n')
        file_out.write('<\%s>\n' %self.tag)

class Html(Element):
    tag = 'html'
    def render(self, file_out, ind=""):
        file_out.write('<%s> \n' %self.tag)
        for item in self.content:
            try:
                item.render(file_out, ind="    ")
            except AttributeError:
                file_out.write(self.indent + ind + item + '\n')
        file_out.write('<\%s>\n' %self.tag)

class Body(Element):
    tag = 'body'
    def render(self, file_out, ind=""):
        file_out.write(ind + '<%s> \n' %self.tag)
        for item in self.content:
            try:
                item.render(file_out, ind="        ")
            except AttributeError:
                file_out.write(self.indent + ind + item + '\n')
        file_out.write(ind + '<\%s>\n' %self.tag)


class P(Element):
    tag = 'p'
    indent = "    "
    def render(self, file_out, ind=""):
        file_out.write(ind + '<%s> \n' %self.tag)
        for item in self.content:
            try:
                item.render(file_out, ind="    ")
            except AttributeError:
                file_out.write(self.indent + ind + item + '\n')
        file_out.write(ind + '<\%s>\n' %self.tag)

class Head(Element):
    tag = 'head'
    def render(self, file_out, ind=""):
        file_out.write(ind + '<%s> \n' %self.tag)
        for item in self.content:
            try:
                item.render(file_out, ind="        ")
            except AttributeError:
                file_out.write(self.indent + ind + item + '\n')
        file_out.write(ind + '<\%s>\n' %self.tag)

class Title(Element):
    tag = 'title'
    indent = "    "
    def render(self, file_out, ind=""):
        file_out.write(ind + '<%s> \n' %self.tag)
        for item in self.content:
            try:
                item.render(file_out, ind="        ")
            except AttributeError:
                file_out.write(self.indent + ind + item + '\n')
        file_out.write(ind + '<\%s>\n' %self.tag)

class Hr(Element):
    tag = 'hr'

    def render(self, file_out, ind=""):
        file_out.write(ind + '<%s \>\n' %self.tag)