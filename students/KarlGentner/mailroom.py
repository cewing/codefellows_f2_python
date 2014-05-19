#!/usr/bin/python


import codecs


# Original donor dict with names and past donations
donorDict = {u'Amy Akin': [[200.32, False], [450.12, False], [565.24, False]],
             u'Bob Bueller': [[3234.44, False], [76348.03, False]],
             u'Carol Carlson': [[101.78, False], [201.92, False], [303.89, False]],
             u'Dave Davis': [[100.45, False], [20.45, False]],
             u'Eve Eastman': [[1200.00, False]]}


# safe input exception handler
def safe_input(message):
    while True:
        try:
            x = raw_input(message)
            return x
        except EOFError:
            return None
        except KeyboardInterrupt:
            return None


# isFloat helper - validate whether string can be cast into a float
def isFloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


# Print donors' names
def printDonors(d):
    print (u"\n")
    print (u"Donors:\n")
    for key in d.iterkeys():
        print(u"{key}").format(key=key)
    print (u"\n")


# Print donors' donations
def printDonations(person):
    print (u"\n")
    print (u"{name}'s donations:\n").format(name=person)
    for (donation, thankCheck) in donorDict[person]:
        print(u"$ {donation}\t Thank You Sent: {thankCheck}").format(donation=str(donation), thankCheck=str(thankCheck))


# For loop for printing all un-written thank you letters.
def printAllBroker():
    for key in donorDict.iterkeys():
        fileNum = 0
        for (donation, thankCheck) in donorDict[key]:
            fileNum += 1
            if thankCheck is False:
                printThankYou(key, donation, fileNum)


# Print thank you letter given a person, donation amount, and file number for naming
def printThankYou(person, amount, fileNum):
    if donorDict[person][fileNum-1][1] is True:
        print(u"\n**** This thank you letter has already been created. ****")
    else:
        thankYouLetter = [u"\n",
                          (u"Dear {name},\n").format(name=person),
                          u"\n",
                          (u"Thank you for your donation of ${donation}.\n").format(donation=str(amount)),
                          u"The world is truly a better place because of people like you.\n",
                          u"\n",
                          u"Sincerely,\n",
                          u"The Charity Foundation\n"]
        filename = (u"{name}{fileNum}.txt").format(name=person, fileNum=str(fileNum))
        f = codecs.open(filename, 'w')
        f.writelines(thankYouLetter)
        f.close()
        print(u"\nThank you letter saved as {name}{fileNum}.txt").format(name=person, fileNum=str(fileNum))
        donorDict[person][fileNum-1][1] = True


# Add Donation interaction. Returns 'm' if user wants to return to previous menu.
def addDonation(person):
    while True:
        print ("\n----------------Add a Donation---------------\n")
        print(u"\nEnter a new or existing donation amount for {name}\n" +
              u"(OR)\n" +
              u"'list' to see {name}'s list of existing donations\n" +
              u"'m' to return to previous menu\n").format(name=person)
        amount = safe_input(u"-->")
        if amount.lower() == u'm':
            return u'm'
        elif amount.lower() == u'list':
            printDonations(person)
            continue
        elif isFloat(amount) is False or amount.startswith('-'):
            print (u"\n\nThat input is not understood. Please try again.\n")
        else:
            amount = round(float(amount), 2)
            print amount
            # If new donation, add  to person's history
            # If not new, determine list placement
            while True:
                choice = safe_input(u"Is this a new donation?(y/n)-->")
                if choice.lower() == u'y':
                    donorDict[person].append([amount, False])
                    fileNum = len(donorDict[person])
                    break
                elif choice.lower() == u'n':
                    fileNum = 0
                    for (donation, thankCheck) in donorDict[person]:
                        fileNum += 1
                        if amount == donation:
                            break
                        elif fileNum == len(donorDict[person]):
                            print (u"\n\n** This donation does NOT already exist - " +
                                   u"Adding amount as new donation.**")
                            donorDict[person].append([amount, False])
                            fileNum = len(donorDict[person])
                            break
                    break
                else:
                    print (u"\n\nThat input is not understood. Please try again.\n")
        # Generate single 'Thank You Letter' for current donation amount
        printThankYou(person, amount, fileNum)


# Send Thank You interaction. Returns 'm' if user wants to return to main menu
def sendThankYou():
    print ("\n---------------Send A Thank You--------------\n")
    while True:
        print(u"\nEnter the full name of an existing donor or new donor\n" +
              u"to create a thank you letter for a new donation.\n" +
              u"(OR)\n" +
              u"'list' to see the list of existing donors\n" +
              u"'a' to create thank you letters for all existing donors\n" +
              u"'m' to return to previous menu\n")
        person = safe_input(u"-->")
        if isFloat(person) is True:
            print (u"\n\nThat input is not understood. Please try again.\n")
        elif person.lower() == u"list":
            printDonors(donorDict)
            continue
        # If 'm' then return to main menu
        elif person.lower() == u'm':
            return u'm'
            # if 'all', print a letter for each donor's donation
        elif person.lower() == u'a':
            printAllBroker()
            continue
        else:
            # if name does not already exist in donor list, add it
            donorDict.setdefault(person, [])
            # Add a donation
            if addDonation(person) == u'm':
                continue


# Create & print report
def createReport():
    print ("\n------------------Report---------------------\n")
    reportDict = {}
    # add new data to report: total, avg, num
    for key in donorDict.iterkeys():
        total = 0.00
        for (donation, thankCheck) in donorDict[key]:
            total += donation
        num = len(donorDict[key])
        if num == 0:
            average = 0.00
        else:
            average = round(total / num, 2)
        reportDict[key] = [total, num, average]

    # create a list from reportDict, sorted by total donation amount
    report = sorted(reportDict.items(), key=lambda donor: donor[1])
    # print report
    for (name, data) in report:
        print (u'{name}\t$ {total:^1}\t{num:^20}\t$ {avg}').format(name=name, total=data[0], num=data[1], avg=data[2])


# Main Menu
def main():
    menu = {u's': sendThankYou, u'c': createReport, u'q': exit}
    print ("\n-----------------Main Menu-------------------\n")
    while True:
        print(u"\n's' to send a thank you\n" +
              u"'c' to create a report\n" +
              u"'q' to quit\n")
        choice = safe_input(u"-->")
        try:
            menu[choice]()
        except KeyError:
            print u"\n\nThat input is not understood. Please try again.\n"


if __name__ == '__main__':
    main()