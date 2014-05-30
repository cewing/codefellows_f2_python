#!/usr/bin/env python


def p_wrapper(func):
	u"""Wrap a string with an html 'p' tag."""

	def wrapped(*args):
		print u'<p>%s</p>' % args
	return wrapped


@p_wrapper
def return_a_string(string):
	return string


if __name__ == "__main__":

	return_a_string(u"This is a string to wrap with a 'p' tag")
	

