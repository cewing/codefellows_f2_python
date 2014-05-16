#!/usr/bin/env python

#mailroom.py

#Mail Merge:  a program for tracking and resonding to donors and donations

"""
INTERPRETER WON'T TAKE DICT SYNTAX... FIX IT HOW?
menu_dict = {('l', 'list'): name_list(),
             ('d', 'donation'): receive_donation() 
             ('r', 'report'): report(donors), 
             ('q', 'quit'): exit(0)}

def start():
    ''' Show menu of actions, receive user instructions on how to proceed '''
    print top_menu
    action = raw_input('What would you like to do: ')
    action.lower()
    for k, v in menu_dict.items():
        if action in k:
            return v
"""

def start():
    ''' Show menu of actions, recieve user instructions on how to proceed '''
    print top_menu
    action = raw_input('What would you like to do: ')
    action.lower()
    if action == u'l' or action == u'list':
        name_list()
        start()
    elif action == u'd' or action == u'donation':
        receive_donation()
        start()
    elif action == u'r' or action == u'report':
        report(donors)
        start()
    elif action == u'q' or action == u'quit':
        exit(0)
    else:
        print u'Did not recognize that response.'
        start()

# Mail is now an automatic part of accepting a donation.
def mail(donor_name):
    #open file w, then print to file...
    print message.format(name=recipient(donor_name), last_donation=last_donation(donor_name))

def recipient(donor_name):
    ''' Return user name for messaging, or add a user if not there '''
    for key in donors.keys():  
        if donor_name == key:
            return key

def check_list(donor_name):
    for key in donors.keys():  
        if donor_name == key:
            return True
        
def last_donation(donor_name):
    ''' Return last donation from a donor '''
    for key, value in donors.items():
        if donor_name == key:
            return value[-1] 

def add_donor(donor_name):
    donors[donor_name] = []

def receive(donor_name):
    ''' Helper to add money once donor is added 
    or found to exist from check_list function '''
    amount = safe_input_num()
    donors[donor_name].append(amount) # FIX
 
# Two safe inputs, one for the name, one for the num.
def safe_input_name(question):
    """Return the correct raw input"""
    try:
        request = raw_input(question)
        return str(request)
    except EOFError:
        print "Got Nothing."
        safe_input_name(request)
    except KeyboardInterrupt:
        print 'Quitting?'
        safe_input_name(request)
    else:
        user_input = raw_input('Please repeat that: ')
    return user_input

def safe_input_num():
    """Return the correct raw input"""
    try:
        request = raw_input(u'Amount given: ')
        if int(request) > 0:
            return request
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        user_input = raw_input('Please repeat that: ')
    return user_input

# Main Menu functions
def receive_donation():
    ''' Add a donation to donor list using helper functions for 
    new or existing donors'''  
    name_request = u"Who gave a donation? (Full Name) >"
    donor_name = safe_input_name(name_request) 
    if check_list(donor_name):
        receive(donor_name)
        mail(donor_name) 
    else:
        print u"Looks like this donor isn't in the list."
        add_donor(donor_name)
        receive(donor_name)
        mail(donor_name)

def name_list():
    ''' Return a list of donor names (only) '''
    for key in sorted(donors.keys()):
        print key

def report(donor_list):
    ''' Print report: Donor name and Total Amount Given '''
    print ''
    table_top = u'Name\t\t\t\tTotal Donation Amount\n'
    print table_top
    for key, value in sorted(donors.iteritems(), key=lambda (k,v): (v,k)):
        print u"%s\t\t\t$%s" % (key, str(sum(value)))
    # sorted([(value,key) for (key,value) in mydict.items()])

# Lists of donor data
donors = {  u'Peter Parker': [10, 20, 30], 
            u'Betty Boop': [30, 50], 
            u'Bruce Wayne':[10000, 20000, 4000],
            u'Mickey Mouse':[1, 2, 3],
            u'Tony Stark':[20000, 40000, 60000, 80000],
            u'Diana Prince':[250, 400, 500],
            u'Bugs Bunny':[40]}


# Strings for different User Actions
top_menu = u'''
The Pythonic Foundation - Thinning out Fat Code for YOU!

WELCOME TO THE MAIL MERGE - TOP MENU

Instructions - Type the first letter of the following:

List - to see a list of donor names
Donation - to receive a donation from a new or existing donor
Report - Create a report of all donors listed by amount given
Quit - to leave the program.

'''

message = u"""

Dear {name}

Though we may be out canvassing various code fat farms, we still
have time to thank you for your exceedingly generous ${last_donation} 
donation.  Though we endeavor to be self sufficient 
in our mission, selling our code drying services to the highest 
bidder, we can always take moment to recognize you with one of 
our self agrandizing emails.  

You deserve nothing less.

Thanks kindly,

Bruce Banner
Executive Director

"""


if __name__ == '__main__':
    start()







