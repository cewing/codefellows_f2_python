#!/usr/bin/python


# Original donor list with names and past donations
donorDict = {u'Amy Akin': [200.32, 450.12, 565.24],
             u'Bob Bueller': [3234.44, 76348.03],
             u'Carol Carlson': [101.78, 201.92, 303.89],
             u'Dave Davis': [100.45, 20.45],
             u'Eve Eastman': [1200.00]}


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


# Print thank You letter for person at index in donor's list.
def printThankYou(person, amount):
    amount = str(int(amount*100))
    amount = (u"{dollars}.{cents}").format(dollars=amount[:len(amount)-2],
                                           cents=amount[len(amount)-2:])
    print (u"\n")
    print (u"Dear {name},\n\n" +
           "Thank you for your recent donation of ${donation}.\n" +
           "The world is truly a better place because of people like you.\n\n" +
           "Sincerely,\n" +
           "The Charity Foundation\n").format(name=person, donation=amount)


# Add Donation interaction. Returns 'm' if user wants to return to main menu.
def addDonation(person):
    while True:
        amount = safe_input(u"Enter the new donation amount\n" +
                            u"'m' to return to main menu\n" +
                            u"-->")
        # Back to main menu
        if amount.lower() == u'm':
            return u'm'
        elif isFloat(amount) is False or amount.startswith('-'):
            print (u"\n\nThat input is not understood. Please try again.\n")
        else:
            # Add donation to person's history
            amount = round(float(amount), 2)
            donorDict[person].append(amount)
            # Generate 'Thank You Letter'
            printThankYou(person, amount)
            return u'm'


# Send Thank You interaction. Returns 'm' if user wants to return to main menu
def sendThankYou():
    while True:
        person = safe_input(u"Enter the full name of an existing donor (OR) new donor\n" +
                            u"'list' to see the list of existing donors\n" +
                            u"'m' to return to main menu\n" +
                            u"-->")
        if isFloat(person) is True:
            print (u"\n\nThat input is not understood. Please try again.\n")
        elif person.lower() == u"list":
            printDonors(donorDict)
            continue
        # If 'm' then return to main menu
        elif person.lower() == u'm':
            return u'm'
        else:
            # if name does not already exist in donor list, add it
            donorDict.setdefault(person, [])
            # Add a donation
            if addDonation(person) == u'm':
                return u'm'


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
        choice = safe_input(u"'s' to send a thank you\n" +
                            u"'c' to create a report (requires full-width window)\n" +
                            u"'q' to quit\n-->")
        try:
            menu[choice]()
        except KeyError:
            print u"\n\nThat input is not understood. Please try again.\n"


if __name__ == '__main__':
    main()