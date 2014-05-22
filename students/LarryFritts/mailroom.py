#!/usr/local/bin/python


"""Mailroom(s) Assignment"""

import codecs

donor_list = {u"Yosemite Sam": [50.25, 150.45],
              u"Elmer Fudd": [190.10, 20.00, 50.76],
              u"Fred Flintstone": [1.],
              u"George Jetson": [256., 567., 7.65],
              u"Barney Rubble": [5.23, 10.10]}

def clean_exit():
    exit(0)

def print_donors(passed_dict):
    """Prints a list of key-values from the passed dict"""
    print u"\n\nCurrent donors:"
    for key in passed_dict.iterkeys():
        print key

def get_donor():

    """Main subroutine of the add donation routine: demonstrates use of dicts and exceptions

    Allows the entering of a new donor or the ability to get a list of current
    donors to pick from. Then passes to add_donation subroutine.
    """

    try:
        user_done = False
        while not user_done:
            print u"\n\nIf you know the name of your donor, please enter it now."
            print u"If you want a list of donor names, please enter 'list'."
            entered_name = raw_input("Donor name or list: ")

            if entered_name == "list":
                print_donors(donor_list)
                entered_name = raw_input(u"\nDonor name: ")

            if entered_name in donor_list:
                add_donation(entered_name)
            else:
                add_donor = raw_input(u"\n\nThat donor does not exist.  Do you want to add %s? " %entered_name)
                while not (add_donor == 'y' or add_donor == 'n'):
                    add_donor = raw_input(u"\nPlease enter 'y' or 'n' ")
                if add_donor == 'y':
                    add_donation(entered_name, True)
                else:
                    continue

            user_cont = raw_input(u"\n\nDo you want to add another donation? (y/n) ")
            while not (user_cont == 'y' or user_cont == 'n'):
                user_cont = raw_input(u"\nPlease enter 'y' or 'n' ")
            if user_cont == 'n':
                user_done = True
    except KeyboardInterrupt:
        clean_exit()


def add_donation(name, new=False):

    """Takes passed name and adds donation or adds new donor and donation
    The flag 'new' alerts the routine to a new donor.
    """
    try:
        amount = raw_input(u"\n\nHow much was donated? ")
        while True:
            try:
                amount = float(amount)
            except ValueError:
                print u"\n\nPlease enter a number!"
                amount = raw_input(u"Amount donated? ")
            else:
                break

        if new:
            donor_list.setdefault(name, [amount])
        else:
            donor_list.get(name).append(amount)

        print u"\n\nAdded %.2f to %s" %(amount, name)
        print u"\n\nCreating 'Thank You' note!"

        thankyou(name, amount)
    except KeyboardInterrupt:
        clean_exit()

def thankyou(name, amount):
    """Prints a thank you letter for a donation"""
    try:
        output_letter = open(name + '.txt', 'w')
        letter = "Dear {}:\n\n\tThank you for your recent donation of ${:.2f}\n\nSincerely, Donation Company".format(name, amount)
        output_letter.write(letter)
    except IOError:
        print u"Unable to open file for writing."

def create_report():
    """Generates report of donor and donor information"""
    try:
        report_dict = build_report_dict()
        print "\n\n"
        print "{:^20} {:<10} {:^10} {:<10}".format(u'Donor', u'Total', u'Times', u'Average')
        for key, value in report_dict.items():
            print "{:<20} ${:<10.2f} {:^10d} ${:<10.2f}".format(key, value[0], value[1], value[2])
        print "\n\n"
    except KeyboardInterrupt:
        clean_exit()

def build_report_dict():
    """Calculates donor information: demonstrates the use of lambda functions"""
    temp_dict = {}
    for key, value in donor_list.items():
        donation_amount = reduce(lambda x,y: x+y, donor_list[key])
        num_donations = len(donor_list[key])
        avg_donation = donation_amount / num_donations
        temp_dict.setdefault(key, [donation_amount, num_donations, avg_donation])

    return temp_dict

def main():
    program_dict = {1: get_donor, 2: create_report, 9: clean_exit}
    while True:
        try:
            print u"\n\n"
            print u"Enter:"
            print u"   '1' to add a donation"
            print u"   '2' to create a report of all donations"
            print u"   '9' to exit program"

            user_input = raw_input()
            program_dict[int(user_input)]()
        except KeyError:
            print u"\nPlease enter a value that corresponds to the choices."

if __name__ == '__main__':
    main()

