#!/usr/bin/python


import copy


# Original donor list with names and past donations
donors = [[u'Amy Akin', [200.32, 450.12, 565.24]],
          [u'Bob Bueller', [3234.44, 76348.03]],
          [u'Carol Carlson', [101.78, 201.92, 303.89]],
          [u'Dave Davis', [100.45, 20.45]],
          [u'Eve Eastman', [1200.00]]]


# safe input exception handler
def safe_input(message):
    while True:
        try:
            x = raw_input(message)
            return x.lower()
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
def printDonors():
    print ("\n")
    print ("Donors:\n")
    for i in range(len(donors)):
        print donors[i][0]
    print ("\n")


# Return index of person in donor's list. Returns -1 if not in list.
def findDonor(person):
    index = -1
    for i in range(len(donors)):
        if person.lower() == donors[i][0].lower():
            index = i
    return index


# Print thank You letter for person at index in donor's list.
def printThankYou(donorIndex, amount):
    amount = str(int(amount*100))
    amount = (u"{dollars}.{cents}").format(dollars=amount[:len(amount)-2],
                                           cents=amount[len(amount)-2:])
    print (u"Dear {name},\n\n" +
           "Thank you for your recent donation of ${donation}.\n" +
           "The world is truly a better place because of people like you.\n\n" +
           "Sincerely,\n" +
           "The Charity Foundation\n").format(name=donors[donorIndex][0], donation=amount)


# Add Donation interaction. Returns 'm' if user wants to return to main menu.
def addDonation(donorIndex):
    amount = ""
    while isFloat(amount) is False and amount != 'm' or amount.startswith('-') is True:
        amount = raw_input("Enter the new donation amount\n" +
                           "'m' to return to main menu\n" +
                           "-->")
    # Back to main menu
    if amount.lower() == 'm':
        return 'm'
    else:
        # Add donation to person's history
        amount = round(float(amount), 2)
        donors[donorIndex][1].append(amount)
        print ("\n")
        # Generate 'Thank You Letter'
        printThankYou(donorIndex, amount)
        return 'm'


# Send Thank You interaction. Returns 'm' if user wants to return to main menu
def sendThankYou():
    # Accept user input: existing donor or new donor
    person = ""
    while person == "" or isFloat(person) is True:
        person = raw_input("Enter the full name of an existing donor (OR) new donor\n" +
                           "'list' to see the list of existing donors\n" +
                           "'m' to return to main menu\n" +
                           "-->")
        # List the donors
        if person.lower() == "list":
            printDonors()
            person = ""
    # Back to main menu
    if person.lower() == 'm':
        return 'm'
    # if name does not already exist in donor list, add it
    donorIndex = findDonor(person)
    if donorIndex < 0:
        donors.append([person, []])
    # Add a donation
    if addDonation(donorIndex) == 'm':
        return 'm'


# Create & print report
def createReport():
    report = copy.deepcopy(donors)
    # add data to new columns of report: total, avg, num
    for i in range(len(report)):
        donations = report[i][1]
        total = 0.00
        for j in range(len(donations)):
            total += round(donations[j], 2)
        num = len(donations)
        if num == 0:
            average = 0.00
        else:
            average = round(total / num, 2)
        report[i].insert(1, average)
        report[i].insert(1, str(num))
        report[i].insert(1, total)
    # sort by total donation amount
    report = sorted(report, key=lambda donor: donor[1])
    # add dollar signs to total & avg
    for i in range(len(report)):
        # ******** This works, but it's admittedly very clunky ********
        report[i][1] = str(int(report[i][1] * 100))
        report[i][1] = "$" + report[i][1][:len(report[i][1])-2] + "." + report[i][1][len(report[i][1])-2:]
        report[i][3] = str(int(report[i][3] * 100))
        report[i][3] = "$" + report[i][3][:len(report[i][3])-2] + "." + report[i][3][len(report[i][3])-2:]
    # print report in table
    print "NAME".rjust(25), "TOTAL DONATIONS".rjust(26),
    print "NUM OF DONATIONS".rjust(27), "AVG DONATION".rjust(28),
    print "\n"
    for i in range(len(report)):
        print report[i][0].rjust(25), report[i][1].rjust(26),
        print report[i][2].rjust(27), report[i][3].rjust(28),
        print "\n"


# Main Interaction
if __name__ == '__main__':
    while True:
        mainMenu = safe_input("'s' to send a thank you\n" +
                              "'c' to create a report (requires full-width window)\n" +
                              "'q' to quit\n-->")
        if mainMenu == 'q':
            break
        elif mainMenu == 's':
            # returns m if user wants to return to main menu
            if sendThankYou() == 'm':
                continue
        elif mainMenu == 'c':
            createReport()
        else:
            print ("\n\nThat input is not understood. Please try again.\n")
