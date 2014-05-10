

def create_dictionary():
	d = {}
	return d
	
create_dictionary()


database = create_dictionary()

def get_name():
	name = raw_input("Enter a first and last name.")
	if name == 'list':
		return database
		name = raw_input("Enter a first and last name")
	if name not in database:
		database.append(name)
		return name
	return name

get_name()


def get_amount():
	amount = raw_input("Enter a donation amount")
	if amount == 'this' :
		amount = raw_input("enter amount")
		database.append(amount)
	else:
		database.append(amount)
		return amount
		
get_amount()


def write_email():
	print "xxxxx"

write_email()