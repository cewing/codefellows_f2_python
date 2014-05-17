#!/usr/bin/env python


from sys import argv
from string import punctuation


script, filename = argv

punct = list(punctuation)
with open(filename) as open_file:
	text = "".join(let.lower() for line in open_file for let in line if let not in punct)

content = text[text.find('the golden bird') : text.find('end of project gutenbergs grimms fairy tales')]
words = content.split()

lookup = {}

