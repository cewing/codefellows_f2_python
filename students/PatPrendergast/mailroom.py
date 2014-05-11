#!usr/bin/env python

#mailroom.py

#Mail Merge:  a program for tracking and resonding to donors and donations


def start():
    ''' Show menu of actions, recieve user instructions on how to proceed '''
    print top_menu
    action = raw_input('What would you like to do: ')
    action.lower()
    if action == u'l' or action == u'list':
        name_list(donors)
        start()
    elif action == u'a' or action == u'add':
        add_donor()
        start()
    elif action == u'm' or action == u'mail':
        mail()
        start()
    elif action == u'r' or action == u'report':
        report(donors)
        start()
    elif action == u'q' or action == u'quit':
        exit(0)
    else:
        print u'Did not recognize that response.'
        start()


# Defining functions for the actions in start()
def mail():
    ''' Show donor list, ask who to message, return message with name and last donation '''
    name_list(donors)
    donor_name = raw_input(u'Which person do you wish to thank today (Full Name)? ')
    print message.format(name=recipient(donor_name), last_donation=last_donation(donor_name))


def recipient(d):
    ''' Return user name for messageing, or add a user if not there '''
    for e in donors:  
        name = e[0]
        if d == name:
            return name 
        

def last_donation(d):
    ''' Return last donation from a donor '''
    for e in donors:
        name = e[0]
        last_donation = e[-1]
        if d == name:
            return last_donation  


def name_list(t):
    ''' Return a list of donor names (only) '''
    for e in t:
        print e[0]
    

def report(t):
    ''' Print report: Donor name and Total Amount Given '''
    print ''
    table_top = u'Name\t\t\t\tTotal Donation Amount\n'
    print table_top
    for e in t:
        name = e[0]
        donations = sum(e[1:])
        print u"%s\t\t\t$%s" % (name, donations)


def add_donor():
    ''' Add a new donor to donors list: Name, amount of donation '''
    print u"Adding a new donor to our Donor's List."
    print''
    new_donor = raw_input("Who are we adding (Full Name)? >")
    print''
    donation = int(raw_input(u'How much did they give? >'))
    print''
    if donation > 0:  #need to add the erroneus input response here.
        donors.append([new_donor, int(donation)])
        print u'{new_donor} has been added.'.format(new_donor=new_donor)
        print''
        '''thanks = raw_input(u"Do you wish to mail a thank you right now? Y or N> "
        if thanks == u'y' or thanks == u'Y':
            print message.format(name=recipient(new_donor), last_donation=last_donation(donation))
        else:
            start()'''
    else:
        print"That is not a number. Donor not added"
        add_donor()



donors = [  [u'Peter Parker', 10, 20, 30], 
            [u'Betty Boop', 30, 50], 
            [u'Bruce Wayne', 10000, 20000, 4000],
            [u'Mickey Mouse', 1, 2, 3],
            [u'Tony Stark', 20000, 40000, 60000, 80000],
            [u'Diana Prince', 250, 400, 500]
]


# Strings for different User Actions
top_menu = u'''
The Pythonic Foundation - Thinning out Fat Code for YOU!

WELCOME TO THE MAIL MERGE - TOP MENU

Intsructions - Type the first letter of the following:

List - to see a list of donor names
Add - to add a donor to the list of donors
Mail - to send a prewritten message to a donor
Report - to see all donors listed by amount given
Quit - to leave the program.

'''

message = u"""
Though we may be out canvassing various code fat farms, we still
have time to thank you, {name}, for your exceedingly 
generous ${last_donation} donation.  Though we endeavor to be self sufficient 
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







