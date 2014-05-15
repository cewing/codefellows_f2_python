#!/usr/bin/env python


def safe_input():
	u"""Return none to an EOFError or KeyboardInterrupt Error."""
	
	while True:
		try:
			reply = raw_input(u'Enter a line of text')
		except(EOFError, KeyboardInterrupt):
			return None
		else:
			return reply
	
safe_input()
