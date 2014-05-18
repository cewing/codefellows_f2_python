#!/usr/bin/env python


from sys import argv
from string import punctuation

script, filename = argv

punct = list(punctuation)
with open(filename) as open_file:
	text = "".join(let.lower() for line in open_file for let in line if let not in punct)

content = text[text.find('the golden bird') : text.find('end of project gutenbergs grimms fairy tales')]
words = content.split()

d = {}

x = [(words[i-2], words[i-1], words[i]) for i in range(len(words) - 1)]

for a, b, c in x:
	d[a, b] = []

for a, b, c in x:
	d[a, b].append(c)

a, b = 'a', 'certain'

new_text = ['a', 'certain']

import random

for i in range(200):
	a, b = b, random.choice(d[tuple([a] + [b])])
	new_text.append(b)

print new_text





















