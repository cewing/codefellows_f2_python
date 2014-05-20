#!/usr/bin/env python


from sys import argv
from string import punctuation

script, filename = argv

punct = list(punctuation)
with open(filename) as open_file:
	text = "".join(let.lower() for line in open_file for let in line if let not in punct)

words = text.split()

lookup = {}

x = [(words[i-2], words[i-1], words[i]) for i in range(len(words) - 1)]

for a, b, c in x:
	lookup[a, b] = []
	
for a, b, c in x:
	lookup[a, b].append(c)


def menu():
	u"""Prompt the user to choose between creating an entire new book or limit the characters to a specified length."""

	action = raw_input(u'Please choose from the following options:\n1. Create an entirely new book\n2. Specify the number of words to generate\n')

	if action == '1':
		length = len(words)
	elif action == '2':
		length = raw_input(u'How many words would you like to generate?\n')
	word_pair(length)


def word_pair(length):
	u"""Ask the user to enter two words to begin the new book."""

	first_word = raw_input(u'Please enter the first word you would like to begin the text\n')
	second_word = raw_input(u'Please enter a second word to follow the first\n')
	generate_text(length, first_word, second_word)


def generate_text(length, first_word, second_word):
	u"""Create new next based on trigram analysis."""

	import random

	while (first_word, second_word) in lookup:

		a, b = first_word.lower(), second_word.lower()
		new_text = [first_word, second_word.lower()]

		for i in range(int(length) + 1):
			try:
				a, b = b, random.choice(lookup[a, b])
				new_text.append(b)
			except KeyError:
				pass

		print u'{text}'.format(text = " ".join(new_text))

		save = raw_input(u'Would you like to save this as a new book?\n1. Yes\n2. No\n')

		if save == '1':
			book_title = raw_input(u'What title would you like for your book?\n')
			with open('new_book.txt', 'w') as new_book:
				new_book.write('{title}\n\n{text}'.format(title = book_title, text = " ".join(new_text))) 
			break
		elif save == '2':
			print u'Thanks and goodbye'
			break

	else:
		print u'That word pair does not exist in the book, please try again.'
		suggestion = random.choice(lookup.keys())
		print u'If you need a word pair, try these: {two_words}'.format(two_words = suggestion)
		return word_pair(length)


menu()

























