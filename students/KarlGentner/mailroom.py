#!/usr/bin/python


import copy


# Create original donor list with names and past donations (in dollars)
donors = [[u'Amy Akin', [200, 450, 565]],
          [u'Bob Bueller', [3234, 763489]],
          [u'Carol Carlson', [101, 200, 300]],
          [u'Dave Davis', [1000000, 20]],
          [u'Eve Eastman', [12345]]]


# isInt - validate whether user input string is an integer
def isInt(userInput):
    try:
        int(userInput)
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


# Print report
def printReport():
    report = copy.deepcopy(donors)
    for i in range(len(report)):
        donations = report[i][1]
        total = 0
        for j in range(len(donations)):
            total += donations[j]
        num = len(donations)
        average = total / num
        report[i].insert(1, str(average))
        report[i].insert(1, str(num))
        report[i].insert(1, str(total))
    x = sorted(report, key=lambda donor: int(donor[1]))
    print ("NAME\t\t\t\tTOTAL DONATIONS\t\tNUM OF DONATIONS\tAVG DONATION\n")
    print ("--------------------------------------------------------------------------------------------")
    for i in range(len(x)):
        print("\t\t\t".join(x[i][0:4]))
        print "\n"


# Print thank You letter for person at index in donor's list.
def printThankYou(index, amount):
    print (u"Dear {name},\n\n" +
           "Thank you for your recent donation of {donation}.\n" +
           "The world is truly a better place because of people like you.\n\n" +
           "Sincerely,\n" +
           "The Charity Foundation\n").format(name=donors[index][0], donation=amount)


# Return index of person in donor's list. Returns -1 if not in list.
def donorIndex(person):
    index = -1
    for i in range(len(donors)):
        if person.lower() == donors[i][0].lower():
            index = i
    return index


# Add donation to person's history using index. Returns 'm' to get to main menu
def addDonation(index):
    userInput = ""
    while isInt(userInput) is False and userInput != 'm':
        userInput = raw_input("Enter the new donation amount\n" +
                              "'m' to return to main menu\n" +
                              "-->").decode()
        # Back to main menu
    if userInput.lower() == 'm':
        return 'm'
    else:
        donors[index][1].append(int(userInput))
        return userInput


# Main Interaction
if __name__ == '__main__':
    # Main Menu
    userInputMain = ""
    while userInputMain != 's' and userInputMain != 'c' and userInputMain != 'q':
        print ("-----------------Main Menu-------------------\n")
        userInputMain = raw_input("'s' to send a thank you\n" +
                                  "'c' to create a report\n" +
                                  "'q' to quit\n-->").decode()
        userInputMain = userInputMain.lower()
        # Quit main menu
        if userInputMain == 'q':
            break
        # Enter 'Send a Thank You' Menu
        while userInputMain == 's':
            print ("---------------Send A Thank You--------------\n")
            userInput = ""
            while userInput == "" or isInt(userInput) is True:
                userInput = raw_input("Enter the full name of an existing donor (OR) new donor\n" +
                                      "'list' to see the list of donors\n" +
                                      "'m' to return to main menu\n" +
                                      "-->").decode()
                # List donors
                if userInput.lower() == "list":
                    printDonors()
                    userInput = ""
            # Back to main menu
            if userInput.lower() == 'm':
                userInputMain = ""
                break
            # if name does not already exist in donor list, add it
            if donorIndex(userInput) < 0:
                donors.append([userInput, []])
            print ("----------------Add a Donation---------------\n")
            amount = addDonation(donorIndex(userInput))
            if amount == 'm':
                userInputMain = ""
                break
            else:
                print ("----------------Thank You Letter-------------\n")
                printThankYou(donorIndex(userInput), amount)
                userInputMain = ""
                break
        # Enter Create a Report Menu
        while userInputMain.lower() == 'c':
            print ("------------------Report---------------------\n")
            printReport()
            # Back to main menu
            userInputMain = ""
            break