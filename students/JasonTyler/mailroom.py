#!/usr/bin/env python
"""Mailroom assignment, version refactored for dictionaries and the like"""
import os


# Donor dictionary where key is verbatim donor name
donors = {
    'Jane R. Goodall': [324, 234],
    'Bob Hunter': [2, 12],
    'Margie L. Smith': [45],
    'Ryan B. McKash': [2345, 234, 1234],
    'Tommy Al Jarrel': [56]
    }


def make_choice():
    """Prompt user to choose an action"""
    choices = {
        '1': send_thankyou,
        '2': create_report,
        '3': batch_print,
        'q': quit_mailroom
    }

    print "Make a choice"
    print "1 to Send a Thank You"
    print "2 to Create Report"
    print "3 to Batch Write Letters to File from Total Donations"
    print "q to Quit"

    user_choice = get_input()
    try:
        choices.get(user_choice)()
    except (KeyError, TypeError):
        print "Try again..."    
    else:
        pass        


def send_thankyou():
    """Format 'Thank You' letter to send to donor"""
    print "Make a choice"
    print "Full name of donor to Send a Thank You"
    print "list to Show List of Donor Names"
    print "b to Return Back"

    user_choice = get_input()
    
    if user_choice == "b": 
        return make_choice()       
    elif user_choice == 'list':
        print_donor_names()
    else:
        if user_choice in donors:
            donor_list = get_donor(user_choice)
            add_donation(donor_list)
            print return_thankyou(user_choice)
        else:
            create_donor(user_choice)
            print return_thankyou(user_choice)
    
    return send_thankyou()


def create_report():
    """
    Create a report of all donor donations

    columns:
    -----
    name     total donated    number of donations    avg donation
    -----
    """
    report_list = list()
    for name, donation_list in donors.items():
        total = str(get_total_donation(donation_list))
        number = str(get_number_donations(donation_list))
        avg = str(get_average_donation(donation_list))
        report_list.append([name, total, number, avg])
    print "\n",
    print "name\t\ttotal\tnumber\taverage"
    print "----------------------------------------"
    # Sorting from highest total donations to least
    report_list = reversed(sorted(report_list, key=lambda element:int(element[1])))    
    for row in report_list:
        print "\t".join(row)
    print "\n",

def return_thankyou(donor_name):
    """Return a donor 'Thank You' message"""
    try:
        donation_list = get_donor(donor_name)
    except TypeError:
        return None
    else:
        message = \
        """
        Dear {name},

        Thank you for your very kind donation of ${last_donation}, 
        it is much appreciated.
        
        Sincerely, 
        NonProfit.notCom
        """.format(name=donor_name, last_donation=donation_list[len(donation_list) - 1]) 

        return message


def create_donor(name, donation=None):
    """Create a new donor and return donation_list"""
    if not donation:
        donors[name] = [get_donation()]
        return donors[name]
    else:
        donors[name] = [donation]
        return donors[name]


def get_donor(user_choice):
    """Get donor donation list"""
    try:
        donor_donation = donors.get(user_choice)
    except (TypeError, KeyError):
        return None
    else:
        return donor_donation


def get_donation():
    """Prompt for and validate donation amount"""
    while True:
        print "Enter a donation amount"
        donation = get_input()
        try:
            donation = float(donation)
        except ValueError:
            pass
        else:
            return donation


def add_donation(donation_list, donation=None):
    """Add a donation to a donation_list"""
    if donation is None:
        donation = get_donation()
    else:
        pass

    try:
        donation_list.append(donation)
    except (AttributeError, TypeError):
        return False
    else:
        return True    


def get_average_donation(donation_list):
    """Get average donation for a donor from donation_list"""
    total = get_total_donation(donation_list)
    number = get_number_donations(donation_list)
    return total/number


def get_total_donation(donation_list):
    """Get total donation for a donor from donation_list"""
    total = 0
    for donation in donation_list:
        if isinstance(donation, (int, float)):
            total += int(donation)
        else:
            pass
    return total


def get_number_donations(donation_list):
    """Get number of donations for a donor from donation_list"""
    return (len(donation_list))


def print_donor_names():
    """Print list of donor names to terminal"""
    print donors.keys()


def batch_print():
    """Print Thank You's for all donors to file in ./mailroom_letters/"""
    working_dir = os.path.split(os.path.realpath(__file__))
    letters_dir = os.path.join(working_dir[0], "mailroom_letters")
    # Attempting to make ./mailroom_letters dir, should it not exist. 
    if not os.path.isdir(letters_dir):
        os.mkdir(letters_dir)
    else:
        pass

    for donor in donors:
        donor_file = os.path.join(letters_dir, "{}.txt".format(donor))
        f = open(donor_file, 'w+')
        f.write(return_thankyou(donor))
        f.close()
    print "'Thank You' files written to disk."


def get_input():
    """Safely get user input and strip whitespace on ends"""
    try:
        user_in = raw_input(">>> ").strip()
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return user_in


def quit_mailroom():
    """Exit out of mailroom module"""
    exit(0)


if __name__ == "__main__":
    # User interaction; exit via a call to quit_mailroom() or external interrupt
    while True:
        make_choice()

