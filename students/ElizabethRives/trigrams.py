#!/usr/bin/env python


from sys import argv
from string import punctuation

script, filename = argv

punct = list(punctuation)
with open(filename) as open_file:
	text = "".join(let.lower() for line in open_file for let in line if let not in punct)

content = text[text.find(u'the golden bird') : text.find(u'end of project gutenbergs grimms fairy tales')]
words = content.split()

d = {}

x = [(words[i-2], words[i-1], words[i]) for i in range(len(words) - 1)]

for a, b, c in x:
	d[a, b] = []

for a, b, c in x:
	d[a, b].append(c)

action = raw_input(u'Please choose from the following options:\n1. Create an entirely new book\n2. Specify the number of words to generate\n')

if action == '1':
	length = len(words)
elif action == '2':
	length = raw_input(u'How many words would you like to generate?\n')

first_word = raw_input(u'Please enter the first word you would like to begin the text\n')
second_word = raw_input(u'Please enter a second word to follow the first\n')

a, b = first_word.lower(), second_word.lower()

new_text = [first_word, second_word.lower()]

import random

for i in range(int(length) + 1):
	a, b = b, random.choice(d[tuple([a] + [b])])
	new_text.append(b)

with open('new_book.txt', 'w') as new_book:
	new_book.write(u'{}'.format(" ".join(new_text)))





















