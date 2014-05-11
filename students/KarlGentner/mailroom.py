#!/usr/bin/python


# Create original donor list with names and past donations (in dollars)
donors = [[u'Amy Akin', [1]],
          [u'Bob Bueller', [10, 20]],
          [u'Carol Carlson', [100, 200, 300]],
          [u'Dave Davis', [1000, 2000]],
          [u'Eve Eastman', [10000]]]


# User pick "Send a Thank You" or "Create a Report"
def userSendCreate():
    userInput = raw_input("type 'S' to send a thank you" +
                          " - OR - type 'C'  to create a report-->").decode()
    userInput = userInput.capitalize()
    while userInput != 'S' and userInput != 'C':
        userInput = raw_input("type 'S' to send a thank you" +
                              " - OR - type 'C'  to create a report-->").decode()
    return userInput
