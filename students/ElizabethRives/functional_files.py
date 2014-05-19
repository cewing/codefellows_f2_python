#!/usr/bin/env python


from sys import argv

script, filename = argv

open_file = open(filename, 'U')
lines = open_file.readlines()


def clean(x):
	"""Remove leading and trailing whitespace from lines in a text file."""

	return [line.strip() for line in x]


action = raw_input('1. Overwrite existing file\n2. Create a new file')

# Using map 

if action == '1':
	y = map(clean, lines)
	open_file = open(filename, 'w')
	open_file.write(str('{}').format("".join(let for line in y for let in line)))
elif action == '2':
	y = map(clean, lines)
	new_filename = raw_input('Enter the name of the file to save it to')
	new_file = open(new_filename, 'w')
	new_file.write(str('{}').format("".join(let for line in y for let in line)))

# Using a list comprehension 

if action == '1':
	clean_lines = [line.strip() for line in open(filename, 'U')]
	open_file = open(filename, 'w')
	open_file.write(str(clean_lines))
elif action == '2':
	clean_lines = [line.strip() for line in open(filename, 'U')]
	new_filename = raw_input('Enter the name of the file to save it to')
	new_file = open(new_filename, 'w')
	new_file.write(str(clean_lines))

