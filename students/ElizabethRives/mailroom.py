#!/usr/bin/env python


state = 'menu'

database = {'Philip Jordan': [500, 200], 'Tom Parker': [750, 800, 750], 'Lisa Smith': [500, 500], 'Wayne Tucker': [400, 500], 'Jane Winkle': [800, 800, 780]}


def menu():
	u"""Prompt the user to either send a thank you email or create a report."""

	print '## -- Type q to exit program or menu to return to main menu -- '
	action = raw_input('Send a Thank You or Create a Report?')
	if action == 'q':
		return 'quit'
	elif action == 'Send a Thank You':
		return 'send a thank you'
	elif action == 'Create a Report':
		return 'create a report'
	else: 
		return menu()
	

def thank_you():
	u"""Add donor name, donation amount to database and compose a thank you email."""

	input_name = raw_input(u'Enter a first and last name\n-- type list to display donors in the database -- ')
	if input_name == 'list':
		print database
		input_name = raw_input(u'Enter a first and last name')
	if input_name == 'menu':
		return 'menu'
	database.setdefault(input_name, [])

	input_amount = raw_input(u'Enter a donation amount')
	if input_amount.isdigit():
		database[input_name].append(int(input_amount))
	elif input_amount == 'menu':
		return 'menu'
	else:
		input_amount = raw_input(u'Enter a donation amount')
		database[input_name].append(int(input_amount))
					
	print u"""Dear %s,\nThank you for your generous donation of $%s. Your contribution will help make the impossible, possible.\nSincerely,\nOrganizationX""" % (input_name, input_amount)

	return 'send a thank you'


def report():
	u"""Display a list of donors sorted by total historical donation amount."""

	d_new = {}

	for key in database.iterkeys():
		name = key
		values = database[key]
		total = sum(values)
		count = len(values)
		average = sum(values)/len(values)
		d_new[name] = (total, count, average)
	
	x = list(d_new.items())

	y = sorted(x, key=lambda a: a[1])

	for (k, v) in y: 
		print u'%s\t %s\t  %s\t%s\t' % (k, v[0], v[1], v[2])

	return 'menu'


lookup = {'1': thank_you, '2': report, 'menu': menu}


if __name__ == '__main__':


	while True:
		if state == 'menu':
			state = lookup['menu']()
		if state == 'send a thank you':
			state = lookup['1']()
		if state == 'create a report':
			state = lookup['2']()
		if state == 'quit':
			break





		


	
			

		






			
		








	


