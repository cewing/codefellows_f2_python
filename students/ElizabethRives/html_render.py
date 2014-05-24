#!/usr/bin/env python


class Element(object):
	""""""

	def __init__(self, content = None, tag = '', ind = ""):
		self.contents = []
		self.content = content
		self.tag = tag
		self.ind = ind
		

	def append(self, content = None):
		"""""" 
		
		self.contents.append(content)


	def render(self, file_out, ind = ""):
		""""""

		file_out.write('%s<%s>\n' % (ind, self.tag))
		for obj in self.contents:
			newind = ind + '  '
			try:
				obj.render(file_out, newind)
			except AttributeError:
				file_out.write('%s%s\n' % (newind, obj))

		file_out.write('%s</%s>\n' % (ind, self.tag))


class Html(Element):
	""""""

	def __init__(self, tag = 'html', ind = 0):
		self.contents = []
		self.tag = tag
		self.ind = ind
	

class Body(Element):
	""""""

	def __init__(self, tag = 'body', ind = 0):
		self.contents = []
		self.tag = tag
		self.ind = ind
	

class P(Element):
	""""""

	def __init__(self, text = None, tag = 'p', ind = 0):
		self.contents = []
		if text != None:
			self.contents.append(text)
		self.tag = tag
		self.ind = ind
	












	







	




	











