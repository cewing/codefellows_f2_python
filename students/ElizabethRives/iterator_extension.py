#!/usr/bin/env python


class Iterator_2(object):

	def __init__(self, start, stop = 5, step = 1):
		self.start = start
		self.current = 0
		self.stop = stop
		self.step = step
	def __iter__(self):
		return self
	def next(self):
		self.current += self.step
		if self.current < self.stop:
			return self.current
		else:
			raise StopIteration
	



if __name__ == "__main__":

	it = Iterator_2(2, 20, 2)

	for i in it:
		if i > 10: break
		print i
	
	for i in it:
		print i