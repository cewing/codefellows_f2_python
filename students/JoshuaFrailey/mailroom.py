import random

random.seed(0)


def _create_donor_list():
    u"""Return a random list of donors and donations."""
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
    u"""Print donor names on same line."""
    donors = _get_donors()
    for i, donor in enumerate(donors):
        if i == len(donors)-1:
            print donor
        else:
            print u"{},".format(donor),


def _add_donor(name):
    u"""Append donor to donor list."""
    donor_list.append([name.title()])


def _add_donation(donor, amount):
    u"""Append donation for donor to donor list."""
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
    for i, donation in enumerate(donations):
        if i == len(donations)-1:
            donations_str += u"$" + unicode(donation)
        else:
            donations_str += u"$" + unicode(donation) + u", "
    return donations_str


def _print_ty_menu():
    u"""Print the 'Send Thank You' sub-menu."""
    menu = []
    menu.append(u"Enter a donor's full name to add a donation and generate")
    menu.append(u"a personalized letter. Type 'list' to see a list of all")
    menu.append(u"donors. Type 'menu' to return to the main menu.")
    for line in menu:
        print line


def _generate_ty(donor):
    u"""Print the thank you letter."""
    donations = _get_donations(donor)
    recent = donations.pop()
    donations.reverse()
    history = _print_donations(donations)
    letter = u"\nDear {},\n\nLocal Chairty is very appreciative".format(donor)
    letter += u" of your recent, generous donation of ${}".format(recent)
    if history:
        letter += u". Much like your previous donations of {},".format(history)
        letter += u" this "
    else:
        letter += u". This "
    letter += u"donation will go to clothe the poor berengas who have been "
    letter += u"so unjustly shermed.\n\nThank you,\n\nLocal Chairty\n"
    print letter


def _send_thankyou():
    u"""Control flow for the 'Send Thank You' sub-menu."""
    _print_ty_menu()
    donor = unicode(raw_input(u"--> ").title())
    while True:
        if donor in [u"Menu", u"M"]:
            break
        elif donor in [u"List", u"L"]:
            _print_donors()
            prompt = u"Type a name from the above list or enter the name of "
            prompt += u"a new donor. Type 'menu' to return to the main menu."
            prompt += u"\n--> "
            donor = unicode(raw_input(prompt).title())
        elif donor in _get_donors():
            _add_amount(donor)
            break
        else:
            while True:
                prompt = u"Do you wish to add a donor named "
                prompt += u"{} (Y/N)? \n--> ".format(donor)
                input_ = unicode(raw_input(prompt))
                if input_.lower() in [u"y", u"yes"]:
                    _add_donor(donor)
                    _add_amount(donor)
                    _generate_ty(donor)
                    break
                else:
                    break
            break


def _add_amount(donor):
    u"""Ask for amount, validate it, and pass it."""
    amount = unicode(raw_input(u"Enter the amount of the donation: "))
    while True:
        if amount in [u"m", u"menu", u"M", u"Menu", u"MENU"]:
            break
        else:
            amount = _is_float(amount)
            _add_donation(donor, amount)
            _generate_ty(donor)
            break


def _is_float(input_):
    u"""Return input_ if it's a float."""
    while True:
        if input_ in [u"m", u"menu", u"M", u"Menu", u"MENU"]:
            break
        try:
            amount = float(input_)
        except ValueError:
            prompt = u"Please only enter a number.\n--> "
            input_ = unicode(raw_input(prompt))
        else:
            return amount


def _create_report():
    u"""Print donation statistics for each donor."""
    print "\n"
    for i, donor in enumerate(donor_list):
        name = donor[0]
        total = sum(donor[1:])
        number = len(donor[1:])
        average = round(sum(donor[1:])/(len(donor[1:])), 2)
        print u"{width}${}{}${}".format(name, total, number, average, width=30)
    print u"\n"


def _print_main_menu():
    u"""Print the the menu options"""
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
