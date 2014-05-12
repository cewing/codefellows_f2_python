#!/usr/bin/python


# Create original donor list with names and past donations (in dollars)
donors = [[u'Amy Akin', [1]],
          [u'Bob Bueller', [10, 20]],
          [u'Carol Carlson', [100, 200, 300]],
          [u'Dave Davis', [1000, 2000]],
          [u'Eve Eastman', [10000]]]


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
    print ("Donors:\n")


# Print report
def printReport():
    print "report"  # to be completed at a later time


# Print thank You letter for person at index in donor's list.
def printThankYou(index, amount):
    print (u"Dear {name},\n\n" +
           "Thank you for your recent donation of {donation}.\n" +
           "The world is truly a better place because of people like you.\n" +
           "Sincerely,\n\n" +
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
    while userInput == "" or isInt(userInput) is False:
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
    userMain = ""
    while userMain != 's' and userMain != 'c' and userMain != 'q':
        print ("-----------------Main Menu-------------------\n")
        userMain = raw_input("'s' to send a thank you\n" +
                             "'c' to create a report\n" +
                             "'q' to quit\n-->").decode()
        userMain = userMain.lower()
        # Quit main menu
        if userMain == 'q':
            break
        # Enter Send a Thank You Menu
        while userMain == 's':
            print ("---------------Send A Thank You--------------\n")
            userSend = ""
            while userSend == "" or isInt(userSend) is True:
                userSend = raw_input("Enter the full name of an existing donor (OR) new donor\n" +
                                     "'list' to see the list of donors\n" +
                                     "'m' to return to main menu\n" +
                                     "-->").decode()
                # List donors
                if userSend.lower() == "list":
                    printDonors()
                    userSend = ""
            # Back to main menu
            if userSend.lower() == 'm':
                userMain = ""
                break
            # Find index of name and add donation
            print ("----------------Add a Donation---------------\n")
            p_index = donorIndex(userSend)
            if p_index >= 0:
                amount = addDonation(p_index)
                if amount == 'm':
                    userMain = ""
                    break
                else:
                    print ("----------------Thank You Letter-------------\n")
                    printThankYou(p_index, amount)
                    userMain = ""
                    break
            # If name is not in list,
            # then add name to list and add donation
            else:
                donors.append([userSend, []])
                p_index = donorIndex(userSend)
                if p_index >= 0:
                    amount = addDonation(p_index)
                    if amount == 'm':
                        userMain = ""
                        break
                    else:
                        print ("-----------------Thank You Letter-----------\n")
                        printThankYou(p_index, amount)
                        userMain = ""
                        break
        # Enter Create a Report Menu
        while userMain.lower() == 'c':
            printReport()
            # Back to main menu
            userMain = ""
            break