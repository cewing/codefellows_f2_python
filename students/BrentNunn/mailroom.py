#!/usr/bin/env python

import codecs

donations = {u"Fred Flinstone": [1000000, 100000, 200000],
             u"Bill Gates": [5],
             u"Linda Blair": [22, 16],
             u"Attila": [0, 0],
             u"Pink Panther": [100, 110]
            }


def get_donation(donor):
    """Get a donation from the donor"""

    while True:
        donation = raw_input(u"Enter donation amount: ")
        if donation.isdigit():
            donation_list = donations.setdefault(donor, [])
            donation_list.append(int(donation))
            print u"Thank you {} for your generosity.".format(donor)
            break
        else:
            print u"Please enter a numeric donation value"


def donation_menu():
    """Menu for thanking donors"""

    while True:
        print u"\n    Enter a donation"
        print u"Enter 'list' to see all past donors"
        print u"Enter 'Q' to Quit"

        name = raw_input(u"Enter a donor's full name: ")

        if name.upper() == 'Q':
            break

        elif name.lower() == "list":
            print u"\nThe donors are: "
            dsorted = donations.keys()
            dsorted.sort()
            for donor in dsorted:
                print donor

        elif len(name) > 0:
            get_donation(name)


def summarize_donor(donor):
    """Summarize donations of a donor"""

    total_donations = 0
    num_donations = 0

    for donation in donations[donor]:
        total_donations += donation
        num_donations += 1
    
    return [donor, total_donations, num_donations, 
        total_donations / num_donations]


def total_donation(row):
    """function used in sorting donors by total donations"""

    return row[1]


def create_report():
    """Create a donors report"""

    donors_summary = []

    for donor in donations:
        donors_summary.append(summarize_donor(donor))

    # Sort the donors by summary of total donations
    donors_summary.sort(key=total_donation)

    print ""
    print u"{:^59}".format("Donor's Summary")

    print "{:<30}{:>12}{:>7}{:>12}".format("Name", "Total", "Count", "Average")
    for row in donors_summary:
        print "{:<30}{:>12,}{:>7,}{:>12,}".format(row[0], row[1], row[2], 
            row[3])


def  create_letters():
    """Create letters of appreciation for the donors' most recent donation"""
    for donation in donations:
        try:
            f = open(donation + ".txt", "w")
            f.write(u"Thank you {} for your donation of {}.\n".format(donation,
                donations[donation][-1]))
            f.close()
        except IOError:
            print u"IO Error writing thank you letters to disk"
        else:
            print u"Thank you letter written to {}.".format(donation)


def safe_input(*prompt):
    """Wrapping raw_input() to catch typical end of input exceptions"""
    try:
        if len(prompt) > 0:
            user_in = raw_input(prompt[0])
        else:
            user_in = raw_input()

    except (KeyboardInterrupt, EOFError):
        return None
    else:
        return user_in


if __name__ == '__main__':
    print u"\nWelcome to the Mail Room, Donors Application."

    while True:
        print u"\n    Main Menu"
        print u"'D' = enter a Donation"
        print u"'R' = create a Report"
        print u"'L' = create Letters thanking donors"
        print u"'Q' = Quit"

        selection = safe_input("\nEnter your selection: ")

        if selection.upper() == 'D':
            donation_menu()
        elif selection.upper() == 'R':
            create_report()
        elif selection.upper() == 'L':
            create_letters()
        elif selection.upper() == 'Q':
            break
        else:
            print(u"Invalid selection")

