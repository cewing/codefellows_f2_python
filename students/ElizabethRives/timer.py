#!/usr/bin/env python


import time


class Timer(object):
	u"""Print to stdout the elapsed time taken to run the code inside the context manager."""

	def __init__(self):
		self.timer = time.time()
	def __enter__(self):
		self.start = self.timer
		return self
	def __exit__(self, *args):
		self.elapsed = time.time() - self.start
		print u'This code took {} seconds'.format(self.elapsed)


if __name__ == "__main__":

	with Timer() as t:
		for i in range(100000):
			i = i * 20



