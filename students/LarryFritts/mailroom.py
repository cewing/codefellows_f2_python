#!/usr/local/bin/python


"""Mailroom(s) Assignment"""

import codecs

donor_list = {u"Larry Fritts": [50.25, 100., 150.45],
              u"Harley Fritts": [190.10, 20.00, 50.76],
              u"Fred Flintstone": [1., 2., 3.],
              u"George Jetson": [256., 34567., 7.65],
              u"Mr. Howell": [2345.23, 5467.55, 10.10]}

def print_donors(passed_dict):
    """Prints a list of key-values from the passed dict"""
    print u"\n\nCurrent donors:"
    for key in passed_dict.iterkeys():
        print key

def get_donor():

    """Main subroutine of the add donation routine

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
                entered_name = raw_input("\nDonor name: ")

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
        exit(0)


def add_donation(name, new=False):

    """Takes passed name and adds donation or adds new donor and donation
    The flag 'new' alerts the routine to a new donor.
    """

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
        donor_list.setdefault(name, amount)
    else:
        donor_list.get(name).append(amount)

    print u"\n\nAdded %.2f to %s" %(amount, name)
    print u"\n\nCreating 'Thank You' note!"

    thankyou(name, amount)

def thankyou(name, amount):
    try:
        output_letter = open(name + '.txt', 'w')
        letter = "Dear {}:\n\n\tThank you for your recent donation of {}\n\nSincerely, Donation Company".format(name, amount)
        output_letter.write(letter)
    except IOError:
        print u"Unable to open file for writing."

def create_report():
    pass
#def main():
get_donor()



#if __init__ == '__main__':
#    main()

