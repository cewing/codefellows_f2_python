#!/usr/bin/env python

donorsANDdollars={u"James Bond":[544,221,444],u"Jackson Pollock":[332,112,3321],u"Keanu Reaves":[444,546,6643,45],u"The Pope":[32,5543,3],u"France":[2345,123,6543,42]}


#def donors(donorsANDdollars):
#    """Generate list of donors from main data structure."""
#    donorsList = []
#    for i in range(len(donorsANDdollars)):
#        donorsList.append(donorsANDdollars[i][0])
#    return donorsList


def selectDonor():
    while True:
        theInput=safe_input(u"Enter a new name or one on the list to send a thank you. Type 'list' to see the list. Name: ")
        if theInput.lower()==u"q":
            return None
        elif theInput == u"list":
            print donorsANDdollars.keys()
        elif theInput in donorsANDdollars:
            return theInput
        elif theInput not in donorsANDdollars:
            donorsANDdollars[theInput]=[]
            return theInput


def getDonationAmount(theDonor):
    while True:
        theInput=safe_input(u"Enter a donation amount as a number: ")
        theInput=unicode(theInput)
        if theInput.lower() == 'q':
            return None
        if theInput.isnumeric():
            for donors in donorsANDdollars:
                if donors==theDonor:
                    theInput=int(theInput)
                    donorsANDdollars[donors].append(theInput)
                    return theInput
        elif theInput==None:
            break
        else:
            print "Please enter a number!"


def send_ThankYou(theDonor,theInput):
    print "Thank you esteemed %s. We greatly appreciate your most recent, and wonderfully generous, donation of %s dollars. Please donate again soon."%(theDonor,theInput)


# I'm guessing there's a way to tidy up the creat_report code, but I'm not exactly sure how yet.
def create_Report():
    donorsANDdollars.values().sort(key=getTotal)

    maxLength1 = max(len(aList) for aList in donorsANDdollars)
    maxLength2 = max(len(str(sum(aList))) for aList in donorsANDdollars.values())
    maxLength3 = max(len(str(len(aList))) for aList in donorsANDdollars.values())

    for aList in donorsANDdollars:
        print aList,
        print (maxLength1-len(aList))*" ",
        print sum(donorsANDdollars[aList]),
        print (maxLength2-len(str(sum(donorsANDdollars[aList]))))*" ",
        print len(donorsANDdollars[aList]),
        print (maxLength3-len(str(len(donorsANDdollars[aList]))))*" ",
        print sum(donorsANDdollars[aList])/len(donorsANDdollars[aList])


def getTotal(aList):
    return -1*sum(aList[:])

def safe_input(text):
    try:
        input = raw_input(unicode(text))
        return input
    except KeyboardInterrupt:
        return None
    except EOFError:
        return None

#####Main Body######
while True:
    choice = safe_input(u"Please input 1 or 2. Send a Thank You(1) or Create a Report(2) (At any time you may enter (Q) to Quit): ")
    if choice == None:
        break
    elif choice == u"1":
        theDonor=selectDonor()
        if theDonor == None:
            break
        theInput=getDonationAmount(theDonor)
        if theInput == None:
            break
        send_ThankYou(theDonor,theInput)
    elif choice == u"2":
        create_Report()
    elif choice.lower() == u"q":
        break
    else:
        print "I did not recognize that response."
