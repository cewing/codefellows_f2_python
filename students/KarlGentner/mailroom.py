#!/usr/bin/python


# Create original donor list with names and past donations (in dollars)
donors = [[u'a', [1]],
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


# Print report
def printReport():
    print "report"  # to be completed at a later time


# Main Interaction
if __name__ == '__main__':
    # Main Menu
    userMain = ""
    while userMain != 's' and userMain != 'c' and userMain != 'q':
        print ("--------------------Main Menu----------------------\n")
        userMain = raw_input("'s' to send a thank you\n" +
                             "'c' to create a report\n" +
                             "'q' to quit\n-->").decode()
        userMain = userMain.lower()
        # Quit main menu
        if userMain == 'q':
            break
        # Enter Send a Thank You Menu
        while userMain == 's':
            userSend = ""
            while userSend == "" or isInt(userSend) is True:
                print ("------------------Send A Thank You-----------------\n")
                userSend = raw_input("'m' to return to main menu\n" +
                                     "'list' to see a list of donors\n" +
                                     "(OR) enter a donor's full name for details\n" +
                                     "-->").decode()
                # List donors
                if userSend.lower() == "list":
                    printDonors()
                    userSend = ""
            # Back to main menu
            if userSend.lower() == 'm':
                userMain = ""
                break
            # A name is entered
            for i in range(len(donors)):
                if userSend.lower() == donors[i][0].lower():
                    person = donors[i]
            print ("\n")
            print person

        # Enter Create a Report Menu
        while userMain.lower() == 'c':
            printReport()
            # Back to main menu
            userMain = ""
            break