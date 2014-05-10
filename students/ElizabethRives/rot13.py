# -*- coding: utf-8 -*-


from string import maketrans

def rot13(s):
	u"""Replace each letter in a text by a letter 13 letters after it in the alphabet."""

	pass_in = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	pass_out = u'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
	table = maketrans(pass_in, pass_out)

	s_rot13 = s.translate(table)
	return s_rot13


if __name__ == '__main__':
	u"""Test that rot13 function performs as expected."""
	
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

	]

	for s, output in vals:
		assert rot13(s) == output
	print u'All Tests Passed'













