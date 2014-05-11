def send_thank_you_note(donor_list):
    #print donor_list
    input_string = raw_input("Enter the full name of a donor, or type 'list' to see a list of donors: ")

    # Print just the donor names, then reprompt user for a name
    while input_string == 'list':
        for a in donor_list:
            print a[:1]
        input_string = raw_input("Enter the full name of a donor, or type 'list' to see a list of donors: ")

    

if __name__ == '__main__':

    # Establish initial donor data, which is a list of lists
    donor_list = [ 
        ['Alan Alda', 5, 10, 15],
        ['Bob Barker', 1000, 5000, 15000],
        ['Cindy Crawford', 75, 250, 600],
        ['David Duchovny', 91, 38, 7],
        ['Emilio Esteves', 70, 70, 70]
        ]

    print u""
    print u"*** Welcome To Mailroom Madness ***"
    print u""
    print u"Menu Options:"
    print u"Type 1 to send a thank you note"
    print u"Type 2 to create a report"
    input_string = int(raw_input('Enter 1 or 2: '))

    # Validate inputs
    while input_string < 1 or input_string > 2:
        print u"Valid options are 1 or 2: "
        input_string = int(raw_input())
    print u""

    # Send Thank You Note
    if input_string == 1:
        send_thank_you_note(donor_list)



