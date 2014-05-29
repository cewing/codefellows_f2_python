# -*- coding: utf-8 -*-


def make_list(n):
	functions = []
	for i in range(n):
		functions.append(lambda x, i=i: i + x)
	return functions

make = make_list(5)

for f in make:
	print f(5)
