#!/usr/bin/env python

donations = [[u"Fred Flinstone", 1000000],
             [u"Bill Gates", 5],
             [u"Linda Blair", 22],
             [u"Attila", 0],
             [u"Pink Panther", 100],
             [u"Linda Blair", 16],
             [u"Fred Flinstone", 100000],
             [u"Attila", 0],
             [u"Pink Panther", 110],
             [u"Fred Flinstone", 200000]]

donors = []


def update_donors_list():
    """Maintain the list of unique donors' names"""

    for donation in donations:
        if donation[0] not in donors:
            donors.append(donation[0])

    donors.sort()


def get_donation(donor):
    """Get a donation from the donor"""

    while True:
        donation = raw_input(u"Enter donation amount: ")
        if donation.isdigit():
            donations.append([donor, int(donation)])
            print u"Thank you {} for your generosity.".format(donor)
            break
        else:
            print u"Please enter a numeric donation value"


def thanks_menu():
    """Menu for thanking donors"""

    update_donors_list()

    while True:
        print u"\n    Send a Thank You"
        print u"Enter 'list' to see all past donors"
        print u"Enter 'Q' to Quit"

        name = raw_input(u"Enter a donor's full name: ")
        if name == 'Q' or name == 'q':
            break
        elif name.lower() == "list":
            print u"\nThe donors are: "
            for donor in donors:
                print donor
        elif len(name) > 0:
            get_donation(name)
            if name not in donors:
                update_donors_list()


def summarize_donor(donor):
    """Summarize donations of a donor"""

    total_donations = 0
    num_donations = 0

    for donation in donations:
        if donation[0] == donor:
            total_donations += donation[1]
            num_donations += 1
    
    return [donor, total_donations, num_donations, total_donations / num_donations]


def total_donation(row):
    """function used in sorting donors by total donations"""

    return row[1]


def create_report():
    """Create a donors report"""

    update_donors_list()
    donors_summary = []

    for donor in donors:
        donors_summary.append(summarize_donor(donor))

    # Sort the donors summary on total donations
    donors_summary.sort(key=total_donation)

    print ""
    print u"{:^59}".format("Donor's Summary")

    print "{:<30}{:>12}{:>7}{:>12}".format("Name", "Total", "Count", "Average")
    for row in donors_summary:
        print "{:<30}{:>12,}{:>7,}{:>12,}".format(row[0], row[1], row[2], row[3])


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
    print u"'T' = send a Thank-you"
    print u"'R' = create a Report"
    print u"'Q' = Quit"

    selection = safe_input("\nEnter your selection: ")

    if selection == 'T' or selection == 't':
        thanks_menu()
    elif selection == 'R' or selection == 'r':
        create_report()
    elif selection == 'Q' or selection == 'q':
        break
    else:
        print(u"Invalid selection")

