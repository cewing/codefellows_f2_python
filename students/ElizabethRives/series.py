# -*- coding: utf-8 -*-


def fibonnaci(n):
	u"""return the nth value in the fibonnaci series."""

	a, b = 0, 1
	
	for i in range(n):
		a, b = b, a + b
	return a


def lucas(n):
	u"""return the nth value in the lucas numbers."""

	a, b = 2, 1

	for i in range(n):
		a, b = b, a + b
	return a


def sum_series(n, a = 0, b = 1):
	u"""return the nth value in the fibonnaci series, lucas numbers or a new series.

	Args: 
	  n: The nth integer. 
	  a(int, optional): The first value in a series. Defaults to 0. 
	  b(int, optional): The second value in a series. Defaults to 1.

	Returns:
	  int: The nth value in the corresponding series. 

	"""

	for i in range(n):
		a, b = b, a + b
	return a


if __name__ == '__main__':
	u"""test that fibonnaci, lucas and sum_series functions perform as expected."""

	vals_fib = [

	(0, 0),
	(1, 1),
	(2, 1),
	(3, 2),
	(4, 3),
	(5, 5),
	(6, 8),
	(7, 13),
	(8, 21),
	(9, 34),
	(10, 55),
	(11, 89),
	(12, 144),
	(13, 233),
	(14, 377),
	(15, 610),
	(16, 987),
	(17, 1597),
	(18, 2584),
	(19, 4181),
	(20, 6765),

	]

	vals_lucas = [

	(0, 2),
	(1, 1),
	(2, 3),
	(3, 4),
	(4, 7),
	(5, 11),
	(6, 18),
	(7, 29),
	(8, 47),
	(9, 76),
	(10, 123),
	(11, 199),
	(12, 322),
	(13, 521),
	(14, 843),
	(15, 1364),
	(16, 2207),
	(17, 3571),
	(18, 5778),
	(19, 9349),
	(20, 15127),
	
	]

	vals_other = [

	(0, 1, 0, 0),
	(0, 1, 1, 1),
	(0, 1, 2, 1),
	(0, 1, 3, 2),
	(0, 1, 4, 3),
	(0, 1, 5, 5),
	(0, 1, 6, 8),
	(0, 1, 7, 13),
	(2, 1, 0, 2),
	(2, 1, 1, 1),
	(2, 1, 2, 3),
	(2, 1, 3, 4),
	(2, 1, 4, 7),
	(2, 1, 5, 11),
	(2, 1, 6, 18),
	(2, 1, 7, 29),
	(3, 4, 0, 3),
	(3, 4, 1, 4),
	(3, 4, 2, 7),
	(3, 4, 3, 11),
	(3, 4, 4, 18),
	(3, 4, 5, 29),
	(3, 4, 6, 47),
	(3, 4, 7, 76),

	]


	for n, output in vals_fib:
		assert fibonnaci(n) == output

	print u'All Tests Pass'

	for n, output in vals_lucas:
		assert lucas(n) == output

	print u'All Tests Pass'

	for a, b, n, output in vals_other:
		assert sum_series(n, a, b) == output

	print u"All Tests Pass"

	

	



	
	






	

