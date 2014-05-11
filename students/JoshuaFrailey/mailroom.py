import random

random.seed(0)


def _create_donor_list():
    """Return a random list of donors and donatiosn"""
    names = [
        [u"Jonathan Blow"], [u"Markus Persson"], [u"Mike Bithell"],
        [u"Calvin Goble"], [u"Alix Stolzer"], [u"Jeff Vogel"]
        ]
    donor_list = []
    random_name = random.choice(names)
    while (len(donor_list) < 5) and random_name not in donor_list:
        donor_list.append(random_name)
        random_name = random.choice(names)
    for donor in donor_list:
        for donations in range(random.randint(1, 3)):
            donor.append(round(random.random()*10000, 2))
    return donor_list


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
            print donor + u",",  # Can this be done with str.format()?


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
    donations_str = u""
    print len(donations)
    for i, donation in enumerate(donations):
        if i == len(donations)-1:
            donations_str += u"$" + unicode(donation)
        else:
            donations_str += u"$" + unicode(donation) + u", "
    return donations_str


def _print_ty_menu():
    """Print the 'Send Thank You' sub-menu"""
    menu = []
    menu.append(u"Enter a donor's full name to add a donation and generate")
    menu.append(u"a personalized letter. Type 'list' to see a list of all")
    menu.append(u"donors. Type 'menu' to return to the main menu.")
    for line in menu:
        print line


def _generate_ty(donor):
    """Print the thank you letter"""
    donations = _get_donations(donor)
    recent = donations.pop()
    donations.reverse()
    history = _print_donations(donations)
    letter = []
    letter.append(u"Dear {},".format(donor))
    letter.append(u"Local Chairty is very appreciative of your recent,")
    letter.append(u"generous donation of ${}. Much like your previous".format(recent))  # FIgure out formatting
    letter.append(u"donations of {}, this doantion will go to clothe the".format(history))
    letter.append(u"poor berengas who have been so unjustly shermed. \n")
    letter.append(u"Thank you, \n")
    letter.append(u"Local Chairty\n")
    for line in letter:
        print line


def _send_thankyou():
    _print_ty_menu()
    donor = unicode(raw_input("--> ").title())
    while True:
        if donor in [u"Quit", "Q"]:
            break
        elif donor in [u"List", u"L"]:
            _print_donors()
            donor = unicode(raw_input(u"Please type a name from the list above or enter the name of a new donor. ").title())
        elif donor in _get_donors():
            _add_amount(donor)
            break
        else:
            while True:
                unicode(raw_input(u"Do you wish to add {}".format(donor)))
                if donor.lower() in [u"y", u"yes"]:
                    _add_donor(donor)
                    break
                else:
                    break
            break


def _add_amount(donor):
    amount = unicode(raw_input(u"Enter the amount of the donation: "))
    while True:
        if amount.lower() in [u"Q", u"Quit"]:
            break
        if amount.isdigit():
            break
        else:
            amount = unicode(raw_input(u"Please only enter digits. "))
    _add_donation(donor, int(amount))
    _generate_ty(donor)


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


if __name__ == "__main__":
    donor_list = _create_donor_list()
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
