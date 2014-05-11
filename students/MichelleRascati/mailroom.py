#!/usr/bin/env python


def thanks(ty_name):
    """Prompt for donation amount and return amount."""
    amt = u'' + raw_input("What is %s's donation amount? " % ty_name)
    if amt == u'quit':
        return None
    else:
        while True:
            try:
                amt = float(amt)
            except ValueError:
                amt = u'' + raw_input("%s is not a number, please enter \
donation amount [or 'quit']: " % amt)
                if amt == u'quit':
                    return None
            else:
                break
        print "Dear %s, \n \
    Thank you for your donation of $%.2f to our charity.  We appreciate \
your support. \n \
    Sincerely,\n Michelle Rascati" % (ty_name, amt)
        return amt


def create(c_list):
    don_rep = []
    for donor in donations:
        total = sum(donor[1:])
        count = len(donor) - 1
        don_rep.append([donor[0], total, count, total / count])
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
    donations = [[u'Larry', 10.00, 150.50, 75.00],
                [u'Sue', 40.00, 35.00],
                [u'Julie', 35.50],
                [u'Bob', 60.25, 100.00],
                [u'Karen', 83.50, 72.45, 90.25]]
    while True:
        do = u''
        while do not in (u'Send a Thank You', u'Create a Report', u'quit'):
            do = u'' + raw_input("'Send a Thank You' or 'Create a Report'? \
[or 'quit']: ")

        if do == u'Send a Thank You':
            # Prompt for full name
            name = ''
            while name not in [col[0] for col in donations]:
                name = u'' + raw_input("Type full name for Thank You letter or\
 'list' for a list of names. [or 'quit']: ")
                if name == u'list':
                    for val in donations:
                        print val[0]
                elif name == u'quit':
                    break
                elif name not in [col[0] for col in donations]:
                    donations.append([name])
            if not name == u'quit':
                amount = thanks(name)
                if not amount is None:
                    donations[[col[0] for col in donations].index(name)]\
                        .append(amount)
                else:
                    # Remove name if quit thanks()
                    donations.pop()
        elif do == u'Create a Report':
            create(donations)
        elif do == u'quit':
            break
