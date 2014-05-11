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


if __name__ == '__main__':
    donations = [[u'Larry', 10.00, 150.50, 75.00],
                [u'Sue', 40.00, 35.00],
                [u'Julie', 35.50],
                [u'Bob', 60.25, 100.00],
                [u'Karen', 83.50, 72.45, 90.25]]
do = u''
while do not in (u'Send a Thank You', u'Create a Report'):
    do = u'' + raw_input("'Send a Thank You' or 'Create a Report'? ")

if do == u'Send a Thank You':
    # Prompt for full name
    name = ''
    while name not in [col[0] for col in donations]:
        name = u'' + raw_input("Type full name for Thank You letter or 'list'\
for a list of names: ")
        if name == u'list':
            for val in donations:
                print val[0]
        elif name not in [col[0] for col in donations]:
            donations.append([name])
    donations[[col[0] for col in donations].index(name)].append(thanks(name))

elif do == 'Create a Report':
    for i in donations:
        #TODO sort by donation amt
        print i
