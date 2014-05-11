


def create_database():
	u"""Store donor names and donation amounts in a database."""

	d = {'Philip Jordan': [500, 200], 'Tom Parker': [750, 800, 750], 'Lisa Smith': [500, 500], 'Wayne Tucker': [400, 500], 'Jane Winkle': [800, 800, 780]}
	return d
	
database = create_database()


def menu():
	u"""Prompt for user to send a thank you or create a report."""

	print u'-- Press q to exit program or a to return to main menu --'
	action = raw_input(u'Send a Thank You or Create a Report?')
	if action == 'q':
		raise SystemExit
	return action

choice = menu()


while choice == 'Send a Thank You':
	

	def get_name():
		u"""Look up donor by name or add new donor to database."""

		input_name = raw_input(u'Enter a first and last name')
		if input_name == 'list':
			print database
			input_name = raw_input(u'Enter a first and last name')
		if input_name not in database:
			database[input_name] = []
		return input_name

	name = get_name()


	def get_amount():
		u"""Add donation amount, for the above donor to database."""

		input_amount = raw_input(u'Enter a donation amount')
		if input_amount.isdigit():
			database[name].append(int(input_amount))
		else:
			input_amount = raw_input(u'Enter a donation amount')
			database[name].append(int(input_amount))
		return input_amount
		
	amount = get_amount()


	def write_email():
		u"""Compose a thank you email to the donor."""

		print u"""Dear %s, 	

Thank you for your generous donation of $%s. Your contribution will help make the impossible, possible.

Sincerely,

OrganizationX""" % (name, amount)

	write_email()


else: 


	def print_report():
		""""""
		
		print database

	print_report()
		
		








	


