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


def _get_donation():
    pass


def _send_thankyou():
    menu = u"""
        Enter a donor's full name to generate a personalized letter.
        Type 'list' to see a list of all donors.
        """
    donor = unicode(raw_input(menu).title())
    while True:
        if donor in [u"List", u"L"]:
            _print_donors()
            donor = unicode(raw_input(u"Please type a name from the list above or enter the name of a new donor. ").title())
        else:
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


while True:
    menu = u"""
        Please select from the following:
        '1: Send a Thank You'
        '2: Create a Report'
        '3: Exit'
        """
    input_ = unicode(raw_input(menu))
    if input_.lower() in [u'1', u's', u'send a thank you']:
        _send_thankyou()
    elif input_.lower() in [u'2', u'c', u'create a report']:
        _create_report()
    elif input_.lower() in [u'3', u'e', u'exit']:
        break
    else:
        input_ = unicode(raw_input(u"Please enter '1', '2', or '3'"))
