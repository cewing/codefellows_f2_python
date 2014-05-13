#!/usr/bin/env python

"""Mailroom assignment"""

# Each sublist referred to as a 'donor record'
# with structure: [first_name, last_name, donation1, donation2...]
donor_list = [
    ["Jane", "Goodall", 324, 234],
    ["Bob", "Hunter", 2, 3],
    ["Margie", "Smith", 3],
    ["Tommmy", "Jarrel", 56],
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
    donor = get_donor_from_str(user_choice)
    donor_name = parse_str_to_donor_name(user_choice)
    if user_choice == "b": make_choice()
    elif user_choice == 'list':
        print_all_donor_names()
        send_thankyou()
    elif donor:
        add_donation(donor, get_donation())
        print_thankyou(donor)
    elif donor_name:
        donor = create_donor(donor_name)
        add_donation(donor, get_donation())
        print_thankyou(donor)
    else: 
        send_thankyou()
    # Exit function with make_choice call
    make_choice()


def create_report(donor_record):
    """Create a report of all donor donations"""

    # Exit function with make_choice call
    make_choice()


def print_thankyou(donor_record):
    """Print a donor 'Thank You' to console"""
    print """Dear %s,\
          \nThank you for your very kind donation of $%s, it is much appreciated."""\
          % (donor_record[0], donor_record[len(donor_record) -1])


def create_donor(name_tuple, donation=None):
    """Create a new donor and return reference to donor record"""
    try:
        first_name, last_name = name_tuple
    except ValueError:
        return False
    else:
        donor_list.append([first_name, last_name])
        donor = donor_list[len(donor_list) -1]
        if not donation:
            pass
        else:
            add_donation(donor, donation) 
    return donor 


def get_donor(name):
    """Use first_name and last_name to return a donor record"""
    try:
        first_name = name[0]
        last_name = name[1]
    except (TypeError, IndexError):
        return None
    else:
        print first_name
        print name[0]
        for donor_record in donor_list:
            if donor_record[0] == first_name and donor_record[1] == last_name:
                return donor_record
        else: 
            return None


def get_donor_from_str(string):
    """Get donor record from a string"""
    name  = parse_str_to_donor_name(string)
    return get_donor(name)


def parse_str_to_donor_name(string):
    """Take a string and return first_name, last_name"""
    name_list = string.split(" ")
    for element in name_list[:]:
        if element == " " or not element:
            del element
        else:
            pass
    if len(name_list) == 2:
        first, last = name_list[0], name_list[1]
        return (first, last)
    else:
        return None


def get_donation():
    """Prompt for and validate a donation amount"""
    while True:
        print "Enter a donation amount"
        donation = get_input()
        try:
            donation = int(donation)
        except ValueError:
            pass
        else:
            return donation


def add_donation(donor_record, donation):
    """Add a donation to a donor record"""
    valid = isinstance(donation, (int, float))    
    if not valid:
        return False
    else:
        donor_record.append(donation)
        return True

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
        formatted_name = "%s %s" % (i[0], i[1])
        names.append(formatted_name)
    print names
    del names


def get_input():
    """Get user input"""
    return raw_input(">>> ").strip()


def quit_mailroom():
    """Exit out of mailroom"""
    exit(0)


# Start everything off with an initial call
make_choice()

