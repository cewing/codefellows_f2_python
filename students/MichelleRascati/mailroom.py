#!/usr/bin/env python
from safe_input import safe_input


def thanks(don_dict):
    """Return updated donation list with new name and amount"""
    # Prompt for full name, list of names, or quit.  Add a name to don_dict.
    while True:
        name = u'' + safe_input("Type full name for Thank You letter\
or [list] for existing donors. (or [quit]): ")
        if name.lower() == u'list':
            for donor in don_dict.keys():
                print donor
        elif name == u'quit':
            # Exit thanks() and return original don_dict
            return don_dict
        else:
            don_dict.setdefault(name, [])
            break

    # Promt for amount until float
    amount = u'' + safe_input("What is %s's donation amount? \
(or [quit])" % ty_name)
    if amount == u'quit':
        # Exit thanks() and return don_dict w/ possible new name & no donations
        return don_dict
    while True:
        try:
            amount = float(amount)
        except ValueError:
            amt = u'' + safe_input("%s is not a number, please enter \
donation amount [or 'quit']: " % amt)
            if amt == u'quit':
                ##TODO
        else:
            break

        if not amount is None:
            don_dict[name].append(amount), amount



    while True:
            try:
                amt = float(amt)
            except ValueError:
                amt = u'' + safe_input("%s is not a number, please enter \
donation amount [or 'quit']: " % amt)
                if amt == u'quit':
                    break
            else:
                break
        print "Dear %s, \n \
    Thank you for your donation of $%.2f to our charity.  We appreciate \
your support. \n \
    Sincerely,\n Michelle Rascati" % (ty_name, amt)
        return amt


def create(c_list):
    """Print a report of donations."""
    don_rep = []
    for donor in donations.keys():
        total = sum(donations[donor])
        count = len(donations[donor])
        don_rep.append([donor, total, count, total / count])
    don_rep.sort(key=second, reverse=True)
    # Find longest name to use for formatting
    n_long = max([len(col[0]) for col in don_rep])
    print "%*s %8s %8s %8s" % (-n_long, "Name", "Total",
                               "Count", "Average")
    for donor in don_rep:
        print "%*s %8i %8i %8d" % \
            (-n_long, donor[0], donor[1], donor[2], donor[3])


def second(l_list):
    """Return second variable in list."""
    return l_list[1]


if __name__ == '__main__':
    donations = {u'Larry': [10.00, 150.50, 75.00],
                 u'Sue': [40.00, 35.00],
                 u'Julie': [35.50],
                 u'Bob': [60.25, 100.00],
                 u'Karen': [83.50, 72.45, 90.25]}
    while True:
        do = u''
        while do.lower() not in (u'ty', u'cr', u'quit'):
            do = u'' + safe_input("Send a Thank You [ty] or Create a Report \
[cr] or [quit]? ")

        if do.lower() == u'ty':
            thanks()
        elif do.lower() == u'cr':
            create(donations)
        elif do.lower() == u'quit':
            break
