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

def send_thanks():
    """Say thankyou to donors"""

    print u"\nThankyou for your generosity!"


def summarize_donor(donor):
    """Summarize donations of a donor"""

    print u"Summarizing for donor {}".format(donor)

    total_donations = 0
    num_donations = 0

    for donation in donations:
        if donation[0] == donor:
            total_donations += donation[1]
            num_donations += 1

    print "donor_summary = {}".format([donor, total_donations, num_donations, 
                                       total_donations / num_donations])
    
    return [donor, total_donations, num_donations, total_donations / num_donations]


def create_report():
    """Create a donors report"""

    donors = []
    donors_summary = []

    for donation in donations:
        if donation[0] not in donors:
            donors.append(donation[0])
            donors_summary.append(summarize_donor(donation[0]))


    print u"\nHere is your report."
    print u"Donors Summary"
    print donors_summary


if __name__ == '__main__':
    print u"\nWelcome to the Mail Room, Donors Application."

while True:
    print u"\n    Menu"
    print u"T = send a Thankyou"
    print u"R = create a Report"
    print u"Q = Quit"

    selection = raw_input("\nEnter your selection: ")

    if selection == 'T' or selection == 't':
        send_thanks()
    elif selection == 'R' or selection == 'r':
        create_report()
    elif selection == 'Q' or selection == 'q':
        break
    else:
        print(u"Invalid selection")



