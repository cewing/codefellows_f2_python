#!/usr/bin/env python


from rot13 import rot13


def test_translate():

	vals = [

		('a', 'n'),
		('b', 'o'),
		('c', 'p'),
		('d', 'q'),
		('e', 'r'),
		('f', 's'),
		('g', 't'),
		('h', 'u'),
		('i', 'v'),
		('j', 'w'),
		('k', 'x'),
		('l', 'y'),
		('m', 'z'),
		('A', 'N'),
		('B', 'O'),
		('C', 'P'),
		('D', 'Q'),
		('E', 'R'),
		('F', 'S'),
		('G', 'T'),
		('!', '!'),
		(' ', ' '),
		('.', '.'),

	]

	for s, output in vals:
		assert rot13(s) == output

