#!/usr/bin/env python


def thanks(ty_name):
    """What this does"""
    amt = raw_input("What is %s's donation amount? " % ty_name)
    while not amt == float(amt):
        amt = raw_input("%s is not a number, please enter donation \
            amount: " % amt)
    print "Dear %s, \n \
        Thank you for your donation of $%f to our charity.  We appreciate\
        your support. \n \
        Sincerely, \n Michelle Rascati" % (ty_name, amt)


if __name__ == '__main__':
    donations = [['Larry', 10.00, 150.50, 75.00],
                ['Sue', 40.00, 35.00],
                ['Julie', 35.50],
                ['Bob', 60.25, 100.00]
                ['Karen', 83.50, 72.45, 90.25]]
do = u''
while do not in (u'Send a Thank You', u'Create a Report'):
    u'' + raw_input("'Send a Thank You' or 'Create a Report'? ")
if do == u'Send a Thank You':
    # Prompt for full name
    name = u'' + raw_input("Type full name for Thank You letter or 'list'\
        for a list of names: ")
    if name == u'list':
        for val in donations:
            print val[0]
    elif name not in [col[0] for col in donations]:
        donations.append([name])
        thanks(name)
    else:
        thanks(name)
