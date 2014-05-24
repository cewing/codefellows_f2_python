import random
import codecs


def _create_donor_dict():
    u"""Return a random list of donors and donations."""
    names = [
        u"Jonathan Blow", u"Markus Persson", u"Mike Bithell",
        u"Calvin Goble", u"Alix Stolzer", u"Jeff Vogel"
        ]
    donor_dict = {}
    random_name = random.choice(names)
    while (len(donor_dict) < 5):
        if random_name not in donor_dict:
            donor_dict.setdefault(random_name, [])
            random_name = random.choice(names)
        else:
            random_name = random.choice(names)
    for donor in donor_dict:
        for donations in range(random.randint(1, 3)):
            donor_dict[donor].append(round(random.random()*10000, 2))
    return donor_dict


def _get_donors():
    u"""Return a list of donor names."""
    return donor_dict.keys()


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
    donor_dict.setdefault(name, [])


def _add_donation(donor, amount):
    u"""Append donation for donor to donor list."""
    donor_dict[donor].append(amount)


def _get_donations(donor):
    u"""Return donations for a given donor."""
    l = []
    l.extend(donor_dict[donor])
    return l


def _print_donations(donations):
    u"""Print donations for a given donor."""
    list_ = []
    for i, donation in enumerate(donations):
        if i == len(donations)-1:
            list_.append(u"${:,}".format(float(donation)))
        elif i == len(donations)-2:
            list_.append(u"${:,}, and ".format(float(donation)))
        else:
            list_.append(u"${:,}, ".format(float(donation)))
    return "".join(list_)


def _print_ty_menu():
    u"""Print the 'Send Thank You' sub-menu."""
    menu = []
    menu.append(u"Enter a donor's full name to add a donation and generate ")
    menu.append(u"a personalized letter. Type 'list' to see a list of all ")
    menu.append(u"donors. Type 'menu' to return to the main menu.")
    print "".join(menu)


def _generate_ty(donor):
    u"""Print the thank you letter."""
    d = {u"donor": donor, u"donations": _get_donations(donor)}
    d[u"recent"] = d[u"donations"].pop()
    d[u"history"] = _print_donations(d[u"donations"][::-1])
    letter = [u"\nDear {donor},\n\nThe Boranga Protection Society"]
    letter.append(u" is very appreciative")
    letter.append(u" of your recent, generous donation of ${recent}")
    if d[u"history"]:
        letter.append(u". Much like your previous donations of {history},")
        letter.append(" this ")
    else:
        letter.append(u". This")
    letter.append(u" donation will go to clothe the poor borangas who have")
    letter.append(u" been so unjustly shermed.\n\nThank you,\n\nThe B.P.S.\n")
    return "".join(letter).format(**d)


def _send_thankyou():
    u"""Control flow for the 'Send Thank You' sub-menu."""
    _print_ty_menu()
    donor = _safe_reprompt(u"--> ").title()
    while True:
        if donor in [u"Menu", u"M"]:
            break
        elif donor in [u"List", u"L"]:
            _print_donors()
            prompt = u"Type a name from the above list or enter the name of "
            prompt += u"a new donor. Type 'menu' to return to the main menu."
            prompt += u"\n--> "
            donor = _safe_reprompt(prompt).title()
        elif donor in _get_donors():
            _add_amount(donor)
            print _generate_ty(donor)
            break
        else:
            while True:
                prompt = u"Do you wish to add a donor named "
                prompt += u"{} (Y/N)? \n--> ".format(donor)
                input_ = _safe_reprompt(prompt)
                if input_.lower() in [u"y", u"yes"]:
                    _add_donor(donor)
                    _add_amount(donor)
                    print _generate_ty(donor)
                    break
                else:
                    break
            break


def _add_amount(donor):
    u"""Ask for amount, validate it, and pass it."""
    amount = _safe_reprompt(u"Enter the amount of the donation:\n-->")
    while True:
        if amount in [u"m", u"menu", u"M", u"Menu", u"MENU"]:
            break
        else:
            amount = _is_float(amount)
            _add_donation(donor, amount)
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
            input_ = _safe_reprompt(prompt)
        else:
            return amount


def _create_report():
    u"""Print donation statistics for each donor."""
    donor_stats = []
    for i, donor in enumerate(donor_dict):
        donor_stats.append([donor])
        donor_stats[i].append(round(sum(donor_dict[donor]), 2))
        donor_stats[i].append(len(donor_dict[donor]))
        donor_stats[i].append(
            round(sum(donor_dict[donor])/len(donor_dict[donor]), 2)
            )
    donor_stats.sort(key=_second_element, reverse=True)
    print "\n"
    title = [u"{:20}".format(u"Name")]
    title.append(u"{:11}".format(u"Total"))
    title.append(u"{:13}{:12}".format(u"Donations", u"Average"))
    print u" ".join(title)
    for i, donor in enumerate(donor_stats):
        name, total, num, avg = donor[0], donor[1], donor[2], donor[3]
        line = u"{:20}${:<11,}".format(name, total)
        line += u"{:^13}${:<12,}".format(num, avg)
        print line
    print u"\n"


def _second_element(list_):
    return list_[1]


def _print_main_menu():
    u"""Print the the menu options"""
    menu = []
    menu.append(u"Please select from the following: ")
    menu.append(u"1: Send a Thank You")
    menu.append(u"2: Create a Report")
    menu.append(u"3: Print letters for all donors")
    menu.append(u"4: Exit")
    for line in menu:  # Not sure if this is better or worse than using join.
        print line


def _safe_input(prompt):
    u"""Return user input that does not cause KeyboardInterrupt or EOFError."""
    try:
        input_ = raw_input(prompt)
    except (KeyboardInterrupt, EOFError):
        return None
    else:
        return unicode(input_)


def _safe_reprompt(prompt):
    u"""Return user input with reprmopt if input is not proper."""
    input_ = _safe_input(prompt)
    while not input_ or input_.isspace():
        print u"\n'I'm sorry, Dave. I'm afraid I can't do that.'"
        input_ = _safe_input(prompt)
    return input_


def _save_letters():
    u"""Write thank you letters to a file for each donor."""
    for donor in donor_dict:
        f = codecs.open(u"{}.txt".format(donor), "w")
        f.write(_generate_ty(donor))
        f.close()
        print u"Letter for {} saved as {}.txt".format(donor, donor)
    print u"All letters saved!"


if __name__ == "__main__":
    donor_dict = _create_donor_dict()
    main_men_dict = {
        k: _send_thankyou for k in [u'1', u's', u'send a thank you']
        }
    main_men_dict.update(
        zip([u'2', u'c', u'create a report'], [_create_report]*3)
        )
    main_men_dict.update(
        zip([u'3', u'p', u'print'], [_save_letters]*3)
        )
    main_men_dict.update(
        zip([u'4', u'e', u'exit'], [None]*3)
        )
    while True:
        _print_main_menu()
        input_ = _safe_reprompt("--> ")
        if input_ in main_men_dict:
            try:
                main_men_dict[input_]()
            except TypeError:
                break
        else:
            input_ = _safe_reprompt(u"Please enter '1', '2', or '3'\n--> ")
