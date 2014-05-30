#!/usr/bin/env python


import itertools


def intsum(): 
	u"""Generate a sequence that adds the next integer."""

	a = 0
	yield a
	
	for y in itertools.count(1, 1):
		a = a + y
		yield a


def doubler(): 
	u"""Generate a sequence that doubles the previous value."""

	a = 1
	yield a

	while True:
		a = 2 * a
		yield a


def fib():
	u"""Generate the fibonacci series."""
	
	a, b = 0, 1

	while True:
		a, b = b, a + b
		yield a


def prime():
	u"""Simply generate the prime numbers."""

	for i in itertools.count(2, 1):
		for a in range(2, i):
			if i%a == 0:
				break
		else:
			yield i




	














	


