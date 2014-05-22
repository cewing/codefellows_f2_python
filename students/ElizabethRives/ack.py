# -*- coding: utf-8 -*-


def ack(m, n):
	u"""perform the Ackermann's function.

	Args:
	  m(int)
	  n(int)

	Returns:
	  int: Value of Ackermann's function given inputs m, n. 

	Raises:
	  ValueError: If m, n is negative.
	"""
	if m < 0 or n < 0:
		raise ValueError(u'input must be a nonnegative integer.')

	if m == 0:
		return n + 1
	elif n == 0:
		return ack(m - 1, 1)
	
	return ack(m - 1, ack(m, n - 1))


if __name__ == '__main__':
	u"""test that Ackermann's function performs as expected."""

	vals = [
	
	(0, 0, 1),
	(0, 1, 2),
	(0, 2, 3),
	(0, 3, 4),
	(0, 4, 5),
	(1, 0, 2),
	(1, 1, 3),
	(1, 2, 4),
	(1, 3, 5),
	(1, 4, 6),
	(2, 0, 3),
	(2, 1, 5),
	(2, 2, 7),
	(2, 3, 9),
	(2, 4, 11),
	(3, 0, 5),
	(3, 1, 13),
	(3, 2, 29),
	(3, 3, 61),
	(3, 4, 125),

	]

	for m, n, output in vals:
		assert ack(m, n) == output

	print u'All Tests Pass'

