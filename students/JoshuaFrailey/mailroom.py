import random

random.seed(0)

donor_list = [
    [u"Jonathan Blow"], [u"Markus Persson"], [u"Mike Bithell"],
    [u"Calvin Goble"], [u"Alix Stolzer"], [u"Jeff Vogel"]
    ]

for donor in donor_list:
    for donations in range(random.randint(1, 3)):
        donor.append(round(random.random()*10000, 2))


def _get_donors():
    u"""Return a list of donor names."""
    names = []
    for donor in donor_list:
        names.append(donor[0])
    return names


def _print_donors():
    u"""Print donor names on same line"""
    donors = _get_donors()
    for i, donor in enumerate(donors):
        if i == len(donors)-1:
            print donor
        else:
            print donor + ",",  # Can this be done with string formatting?


def _add_donor(name):
    u"""Append donor to donor list."""
    donor_list.append([name.title()])


def _add_donation(donor, amount):
    u"""Append donation for donor to donor list"""
    donors = _get_donors()
    i = donors.index(donor)
    donor_list[i].append(amount)


def _get_donations(donor):
    u"""Return donations for a given donor."""
    donors = _get_donors()
    donor_pos = donors.index(donor)
    return donor_list[donor_pos][1:]


def _print_donations(donations):
    u"""Print donations for a given donor."""
    for i, donation in enumerate(donations):
        if i == len(donations)-1:
            print u"${}".format(donation)
        else:
            print u"${}".format(donation) + ",",


def _print_ty_menu():
    """Print the 'Send Thank You' sub-menu"""
    menu = []
    menu.append(u"Enter a donor's full name to generate a personalized letter")
    menu.append(u"Type 'list' to see a list of all donors.")
    for line in menu:
        print line


def _generate_ty(donor):
    """Print the thank you letter"""
    donations = _get_donations(donor)
    recent = donations[-1]
    history = donations[:len(donations)-1]
    letter = []
    letter.append(u"Dear {},".format(donor))
    letter.append(u"Local Chairty is very appreciative of your recent,")
    letter.append(u"generous donation of {}. Much like your previous".format(recent))  # FIgure out formatting
    letter.append(u"donations of {}, this doantion will go to clothe the".format(history))
    letter.append(u"poor berengas who have been so unjustly shermed. \n")
    letter.append(u"Thank you, \n")
    letter.append(u"Local Chairty")
    for line in letter:
        print line


def _send_thankyou():
    _print_ty_menu()
    donor = unicode(raw_input("--> ").title())
    while True:
        if donor in [u"List", u"L"]:
            _print_donors()
            donor = unicode(raw_input(u"Please type a name from the list above or enter the name of a new donor. ").title())
        else:  # Need to not add a donor if donor exists
            _add_donor(donor)
            break
    amount = unicode(raw_input(u"Enter the amount of the donation: "))
    while True:
        # Need to account for '.'
        if amount.isdigit():
            break
        else:
            amount = unicode(raw_input(u"Please only enter digits. "))
    _add_donation(donor, int(amount))


def _create_report():
    pass


def _print_main_menu():
    """Print the the menu options"""
    menu = []
    menu.append(u"Please select from the following: ")
    menu.append(u'1: Send a Thank You')
    menu.append(u'2: Create a Report')
    menu.append(u'3: Exit')
    for line in menu:
        print line


while True:
    _print_main_menu()
    input_ = unicode(raw_input("--> "))
    if input_.lower() in [u'1', u's', u'send a thank you']:
        _send_thankyou()
    elif input_.lower() in [u'2', u'c', u'create a report']:
        _create_report()
    elif input_.lower() in [u'3', u'e', u'exit']:
        break
    else:
        input_ = unicode(raw_input(u"Please enter '1', '2', or '3'"))
