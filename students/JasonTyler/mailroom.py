"""Mailroom assignment"""

# Each sublist referred to as a 'donor record'
# with structure: [first_name, last_name, donation1, donation2...]
donor_list = [
    ["Jane", "Goodall", 324, 234],
    ["Bob", "Hunter", 2, 3],
    ["Margie", "Smith", 3],
    ["Jarrell", "Tommy", 56],
    ["Ryan", "McKash", 2345, 234, 1234]
]

def make_choice():
    """Prompt user to choose an action"""
    print "Make a choice"
    print "1 to Send a Thank You"
    print "2 to Create Report"
    print "q to Quit"

    user_choice = get_input()
    if user_choice == "1": send_thankyou()
    elif user_choice == "2": create_report()
    elif user_choice == "q": quit_mailroom()
    else: make_choice()

def send_thankyou():
    """Format 'Thank You' letter to send to donor"""
    print "Make a choice"
    print "Full name of donor to Send a Thank You"
    print "list to Show List of Donor Names"
    print "b to Return Back"
 
    user_choice = get_input()
    if user_choice == "b": make_choice()
    elif len(user_choice).split(" ") == 2:
        first = user_choice[0]
        last = user_choice[1]
        donor = get_donor(first, last)
        if not donor:
            get_donation()
            create_donor(first, last)
        else:
            while True:
                print "Enter donation amount"
                donation = get_input()
                if isintance(donation, (int, float)):
                    add_donation(donor, int(donation))
                else:
                    continue


    else: send_thankyou()
    # Exit function with make_choice call

def create_report():
    """Create a report of all donor donations"""

    # Exit function with make_choice call
    make_choice()

def quit_mailroom():
    """Exit out of mailroom"""
    
    # Exit function with make_choice call
    make_choice()

def create_donor(first_name, last_name):
    """Create a new donor and return reference to donor record"""
    pass

def get_donor(first_name, last_name):
    """Use first_name and last_name to return a donor record"""
    for donor_record in donor_list:
        if donor_record[0] == first_name and donor_record[1] == last_name:
            return donor_record
    else: return None 

def get_donor_from_str(first_name, last_name):
    """Get donor record from a string"""
    pass

def add_donation(donor_record, donation):
    """Add a donation to a donor record"""
    pass

def get_average_donation(donor_record):
    """Get average donation from donor record"""
    pass

def get_total_donation(donor_record):
    """Get total donation from donor record"""
    pass

def print_all_donor_names():
    """Print list of donor names to terminal"""
    names = list()
    for i in donor_list:
        formatted_name = "%s %s" % i[0], i[1]    
        names.append(formatted_name)
    print names
    del names

def get_input():
    """Get user input"""
    return raw_input(">>> ").strip()

# Start everything off with an initial call
make_choice()

