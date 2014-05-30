#!/usr/bin/env python


def sum_integers(n): 
	u"""Generate a sequence that adds the next integer."""

	a = 0

	for i in range(-1, n):
		a += i + 1
		yield a


def doubler(n): 
	u"""Generate a sequence that doubles the previous value."""

	a = 1
	yield a

	for i in range(n):
		a = 2 * a
		yield a


def fibonacci(n):
	u"""Generate the fibonacci series."""
	
	a, b = 0, 1

	for i in range(n):
		a, b = b, a + b
		yield a


def prime_numbers(n):
	u"""Simply generate the prime numbers."""

	for i in range(2, n):
		for a in range(2, i):
			if i%a == 0:
				break
		else:
			yield i




	














	


