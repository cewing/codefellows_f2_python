#!usr/bin/env python

#mailroom.py
''' Mail Merge:  a program for tracking and resonding to donors and donations'''


def start():
    print top_menu
    action = raw_input('What would you like to do: ')
    action.lower()
    if action == u'l' or action == u'list':
        name_list(donors)
        start()
    elif action == u'm' or action == u'mail':
        mail()
    elif action == u'r' or action == u'report':
        report(donors)
    elif action == u'q' or action == u'quit':
        exit(0)
    else:
        print u'Did not recognize that response.'
        start()

def mail():
    donor_name = raw_input(u'Which person do you wish to thank today? ')
    donor_info(donor_name)
    print message

def report(t):
    table_top= u'Name\t\t\t\tTotal Donation Amount\n'
    print table_top
    for e in donors:
        print donors[e][0] + '\t\t' + sum(donors[e][1:])

def name_list(t):
    for e in range(t):
        print donors[e][0] # accessing list in list?

def donor_info(d):
    if d in donors:
        donors.index(d)
        return donors[d][0]  # accessing list in list?
    else:
        add_donor(d)

def add_donor(d):
    donors.append([d])
    donation = int(raw_input(u'How much did they give? '))
    donors.append()


top_menu = u'''
Pythonic Florida Foundation - Thinning out Fat Code for YOU!

Welcome to Mail Merge - Top Menu

Intsructions - Type the first letter of the following:

List - to see a list of donor names
Mail - to send a prewritten message to a donor
Report - to see all donors listed by amount given
Quit - to leave the program.

'''

donors = [  [u'Peter Parker', 10, 20, 30], 
            [u'Betty Boop', 30, 50], 
            [u'Bruce Wayne', 100000, 2000000, 400000],
            [u'Mickey Mouse', 1, 2, 3],
            [u'Tony Stark', 20000, 40000, 60000, 80000]]

message = u"""
Though we may be out killing Burmese Pythons, we still
have time to thank you, %s, for your exceedingly 
generous $%s donation.  Though we endeavor to be self sufficient 
in our mission, selling our code drying services to the highest 
bidder, we can always take moment to recognize you with one of 
our self agrandizing emails.  

You deserve nothing less.

Thanks kindly,

Bruce Banner
Executive Director

""" % (donors[0][0], donors[0][-1])

#start()

print message

#if __name__ == '__main__':
    #start()

name_list(donors)

report(donors)



