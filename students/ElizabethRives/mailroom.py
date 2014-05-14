#!/usr/bin/env python


state = 'menu'

database = {'Philip Jordan': [500.0, 200.0], 'Tom Parker': [750.0, 800.0, 750.0], 'Lisa Smith': [500.0, 500.0], 'Wayne Tucker': [400.0, 500.0], 'Jane Winkle': [800.0, 800.0, 780.0]}


def menu():
	u"""Prompt the user to choose from a menu of options."""

	print '## -- Type q to exit program or menu to return to main menu -- '
	action = raw_input('Please choose from the following menu:\n1. Record donors and contribution amounts\n2. Create a Report\n3. Write Letters\n4. View Full Set of Letters\n')
	if action == 'q':
		return 'quit'
	elif action == '1':
		return 'record donors and contribution amounts'
	elif action == '2':
		return 'create a report'
	elif action == '3':
		return 'write letters'
	elif action == '4':
		return 'view full set of letters'
	else: 
		return 'menu'
	

def add_to_database():
	u"""Add donor name and contribution amount to the database."""

	input_name = raw_input(u"Please enter the donor's first and last name\n-- type list to display donors in the database -- ")
	if input_name == 'list':
		print database
		input_name = raw_input(u"Please enter the donor's first and last name")
	if input_name == 'menu':
		return 'menu'
	database.setdefault(input_name, [])

	while True:
		input_amount = raw_input(u'Enter the donation amount')
		if input_amount == 'menu':
			return 'menu'
		try:
			input_amount = float(input_amount)
			break
		except ValueError:
			print 'Donation amount must be a numeric input, please try again.'	
	database[input_name].append(input_amount)

	return 'record donors and contribution amounts'
			
	
def write_letters():
	u"""Write a full set of letters thanking donors for their total contribution."""

	letter_file = open('letterfile.txt', 'w')

	for (k, v) in database.iteritems():
		letter_file.write('Dear {name},\nThank you for your generous donation of ${amount}. Your contribution will help make the impossible, possible.\nSincerely,\nOrganizationX\n\n'.format(name = k, amount = sum(v)))
	
	print u'Done...returning to main menu'
	return 'menu'
    

def view_letters():
	u"""View content of file containing all thank you letters written.""" 

	letter_file = open('letterfile.txt', 'U')
			
	for line in letter_file:
		print line

	return 'menu'


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
		print u'{name}\t {total}\t {count}\t {average}\t'.format(name = k, total = v[0], count = v[1], average = v[2])

	return 'menu'


lookup = {'1': add_to_database, '2': report, '3': write_letters, '4': view_letters, 'menu': menu}


if __name__ == '__main__':


	while True:
		if state == 'menu':
			state = lookup['menu']()
		if state == 'record donors and contribution amounts':
			state = lookup['1']()
		if state == 'create a report':
			state = lookup['2']()
		if state == 'write letters':
			state = lookup['3']()
		if state == 'view full set of letters':
			state = lookup['4']()
		if state == 'quit':
			break
		


	





		


	
			

		






			
		








	


