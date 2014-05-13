#!/usr/bin/env python

donorsANDdollars=[[u"James Bond",544,221,444],[u"Jacksn Pollock",332,112,3321],[u"Keanu Reaves",444,546,6643,45],[u"The Pope",32,5543,3],[u"France",2345,123,6543,42]]
def donors(donorsANDdollars):
    """Generate list of donors from main data structure."""
    donorsList = []
    for i in range(len(donorsANDdollars)):
        donorsList.append(donorsANDdollars[i][0])
    return donorsList

def selectDonor():
    while True:
        theInput=raw_input(u"Enter a new name or one on the list to send a thank you. Type 'list' to see the list. Name: ")
        if theInput == u"list":
            print donors(donorsANDdollars)
        elif theInput in donors(donorsANDdollars):
            return theInput
        elif theInput not in donors(donorsANDdollars):
            donorsANDdollars.append([theInput])
            return theInput

def getDonationAmount(theDonor):
    while True:
        theInput=raw_input(u"Enter a donation amount as a number: ")
        theInput=unicode(theInput)
        if theInput.isnumeric():
            for donors in donorsANDdollars:
                if donors[0]==theDonor:
                    theInput=int(theInput)
                    donors.append(theInput)
                    return
        else:
            print "Please enter a number!"



def create_Report():
    pass



for i in range(len(donorsANDdollars)):
    answered=0
    while answered == 0:
        choice = raw_input(u"Please input 1 or 2. Send a Thank You(1) or Create a Report(2): ")
        if choice == u"1":
            theDonor=selectDonor()
            getDonationAmount(theDonor)
            print donorsANDdollars
            #send_ThankYou()
            answered=1
        elif choice == u"2":
            create_Report()
            answered=1
