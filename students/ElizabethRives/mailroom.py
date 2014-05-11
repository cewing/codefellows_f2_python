


def create_database():
	d = []
	return d
	
create_database()

database = create_database()


def menu():
	action = raw_input(u'Send a Thank You or Create a Report?')
	return action

menu()

choice = menu()

while choice == 'Send a Thank You':
	

	def get_name():
		input_name = raw_input(u'Enter a first and last name')
		if input_name == 'list':
			return database
			input_name = raw_input(u'Enter a first and last name')
			return input_name
		if input_name not in database:
			database.append(input_name)
			return input_name
		return input_name

	get_name()

	name = get_name()


	def get_amount():
		input_amount = raw_input(u'Enter a donation amount')
		if input_amount == 'this':
			input_amount = raw_input(u'Enter a donation amount')
			database.append(input_amount)
		else:
			database.append(input_amount)
			return input_amount
		
	get_amount()

	amount = get_amount()


	def write_email():
		print u"xxxxx"

	write_email()


else: 


	def print_report():
		print u'yyyyyyyy'

	print_report()







	


