#!/usr/bin/env python
from safe_input import safe_input
import codecs


def thanks(don_dict):
    """Return updated donation list with new name and amount"""
    # Prompt for full name, list of names, or quit.  Add a name to don_dict.
    while True:
        name = u'' + safe_input("Type full name for Thank You letter \
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
(or [quit]) " % name)
    if amount == u'quit':
        # Exit thanks() and return don_dict w/ possible new name & no donations
        return don_dict
    while True:
        try:
            amount = float(amount)
        except ValueError:
            amount = u'' + safe_input("%s is not a number, please enter \
donation amount [or 'quit']: " % amount)
            if amount == u'quit':
                return don_dict
        else:
            break

    # Add amount to current donor's list
    don_dict[name].append(amount)

    l_file = "./mail/{}_ty.txt".format(name)
    letter = codecs.open(l_file, 'w')
    letter.write("Dear {}, \n\n\
\tThank you for your donation of ${:.2f} to our charity.  We appreciate \
your support.\n\n\
Sincerely,\nMichelle Rascati".format(name, amount))
    letter.close()
    return don_dict


def create(c_list):
    """Print a report of donations."""
    don_rep = []
    # Number of spaces in case of long names
    n_long = 8
    for donor in donations.keys():
        if len(donor) > n_long:
            n_long = len(donor)
        total = sum(donations[donor])
        count = len(donations[donor])
        if count == 0:
            avg = 0
        else:
            avg = total / count
        don_rep.append([donor, total, count, avg])
    # Sort list by Total amount, greatest first
    don_rep.sort(key=second, reverse=True)

    print "{name:<{n}} {total:>8} {count:>8} {average:>8}".\
        format(n=n_long, name="Name", total="Total",
               count="Count", average="Average")
    for donor in don_rep:
        print "{name:<{n}} {total:>8.2f} {count:>8} {average:>8.2f}".\
            format(n=n_long, name=donor[0], total=donor[1],
                   count=donor[2], average=donor[3])


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
            donations = thanks(donations)
        elif do.lower() == u'cr':
            create(donations)
        elif do.lower() == u'quit':
            break
