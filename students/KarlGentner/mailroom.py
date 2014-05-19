#!/usr/bin/python


import codecs


# Original donor list with names and past donations
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


# Print the list of donors' names
def printDonors(d):
    print (u"\n")
    print (u"Donors:\n")
    for key in d.iterkeys():
        print(u"{key}").format(key=key)
    print (u"\n")


# Print the list of donors' donations
def printDonations(person):
    print (u"\n")
    print (u"{name}'s donations:\n").format(name=person)
    for (donation, thankCheck) in donorDict[person]:
        print(u"$ {donation}\t Thank You Sent: {thankCheck}").format(donation=str(donation), thankCheck=str(thankCheck))


# Print thank You letter given a person and donation amount.
# If fullSet = True, then the donation amount is a sum of all donations.
# and the word "combined" is added to the letter
def printThankYou(person, amount, fileNum):
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


# Add Donation interaction. Returns 'm' if user wants to return to main menu.
def addDonation(person):
    while True:
        print(u"\nEnter a new or existing donation amount for {name}\n" +
              u"(OR)\n" +
              u"'list' to see {name}'s list of existing donations\n" +
              u"'p' to return to previous menu\n").format(name=person)
        amount = safe_input(u"-->")
        if amount.lower() == u'p':
            return u'p'
        elif amount.lower() == u'list':
            printDonations(person)
            continue
        elif isFloat(amount) is False or amount.startswith('-'):
            print (u"\n\nThat input is not understood. Please try again.\n")
        else:
            amount = round(float(amount), 2)
            # If new donation, add  to person's history
            while True:
                selection = safe_input(u"Is this a new donation?(y/n)-->")
                if selection.lower() == u'y':
                    tempList = [amount, False]
                    donorDict[person].append(tempList)
                    fileNum = len(donorDict[person])
                    break
                elif selection.lower() == u'n':
                    fileNum = 0
                    for (donation, thankCheck) in donorDict[person]:
                        fileNum += 1
                        if amount == donation:
                            break
                    break
                else:
                    print (u"\n\nThat input is not understood. Please try again.\n")
            # Generate single 'Thank You Letter' for current donation amount
            printThankYou(person, amount, fileNum)
            continue


# Send Thank You interaction. Returns 'm' if user wants to return to main menu
def sendThankYou():
    while True:
        print(u"\nTo create a thank you letter for a new donation,\n" +
              u"enter the full name of an existing donor or new donor\n" +
              u"(OR)\n" +
              u"'list' to see the list of existing donors\n" +
              u"'a' to create thank you letters for all existing donors\n" +
              u"'p' to return to previous menu\n")
        person = safe_input(u"-->")
        if isFloat(person) is True:
            print (u"\n\nThat input is not understood. Please try again.\n")
        elif person.lower() == u"list":
            printDonors(donorDict)
            continue
        # If 'm' then return to main menu
        elif person.lower() == u'p':
            return u'p'
            # if 'all', print a letter for each donor's donation
        elif person.lower() == u'a':
            for key in donorDict.iterkeys():
                fileNum = 0
                for (donation, thankCheck) in donorDict[key]:
                    fileNum +=1
                    if thankCheck is False:
                        printThankYou(key, donation, fileNum)
            continue
        else:
            # if name does not already exist in donor list, add it
            donorDict.setdefault(person, [])
            # Add a donation
            if addDonation(person) == u'p':
                continue


# Create & print report
def createReport():
    reportDict = {}
    # add new data to report: total, avg, num
    for key in donorDict.iterkeys():
        donations = donorDict[key]
        total = sum(donations)
        num = len(donations)
        if num == 0:
            average = 0.00
        else:
            average = round(total / num, 2)
        reportDict[key] = [total, num, average]

    # create a list from reportDict, sorted by total donation amount
    report = sorted(reportDict.items(), key=lambda donor: donor[0])
    # print report
    for (name, data) in report:
        print (u'{name}\t\t$ {total:<1}\t\t{num}\t$ {avg}').format(name=name, total=data[0], num=data[1], avg=data[2])


# Main Menu
def main():
    menu = {u's': sendThankYou, u'c': createReport, u'q': exit}
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