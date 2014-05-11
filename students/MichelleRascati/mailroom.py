#!/usr/bin/env python


def thanks(ty_name):
    """Prompt for donation amount and return amount"""
    amt = raw_input("What is %s's donation amount? " % ty_name)
    while True:
        try:
            amt = float(amt)
        except ValueError:
            amt = raw_input("%s is not a number, please enter donation \
amount: " % amt)
        else:
            break
    #while not amt == float(amt):
    #    amt = raw_input("%s is not a number, please enter donation \
    #        amount: " % amt)
    print "Dear %s, \n \
Thank you for your donation of $%.2f to our charity.  We appreciate \
your support. \n \
Sincerely,\n Michelle Rascati" % (ty_name, amt)
    return amt


def second(l_list):
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
                elif name not in [col[0] for col in donations]:
                    donations.append([name])
                elif name == u'quit':
                    break
            if not name == u'quit':
                donations[[col[0] for col in donations].index(name)].append(
                    thanks(name))

        elif do == u'Create a Report':
            new_dons = []
            for donor in donations:
                total = sum(donor[1:])
                count = len(donor) - 1
                new_dons.append([donor[0], total, count, total / count])
            new_dons.sort(key=second, reverse=True)
            # Find longest name to use for formatting
            n_long = max([len(col[0]) for col in new_dons])
            for donor in new_dons:
                print "%*s Total: %8i Count: %8i Average: %8d" % \
                    (-n_long, donor[0], donor[1], donor[2], donor[3])
        elif do == u'quit':
            break
