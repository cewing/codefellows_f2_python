def send_thank_you_note(donor_list):
    """Allow user to make additions to donor data, and generate a thnk you note"""
    input_string = raw_input("Enter the full name of a donor, or type 'list' to see a list of donors: ")

    # Print just the donor names, then reprompt user for a name
    while input_string == 'list':
        for a in donor_list:
            print a[0]
        input_string = raw_input("Enter the full name of a donor, or type 'list' to see a list of donors: ")

    # Create a new list just of donor names
    donor_list_names = []
    for a in donor_list:
        donor_list_names.append(a[0])

    # If donor not already in list, add the new donor
    if input_string not in donor_list_names:
        print u"Adding %s to donor list." % input_string
        donor_list.append([input_string])

    # Promt user for a donation amount for current donor, and add it to that donor's donation history
    input_donation = raw_input("Enter a donation amount for %s: " % input_string)

    #Check to see if input is a number, reprompt if not


    for a in donor_list:
        if a[0] == input_string:
            a.append(int(input_donation))

    print donor_list

def create_report():
    """Print list of donors, sorted by total historical donation amount"""
    return


if __name__ == '__main__':

    # Establish initial donor data, which is a list of lists
    donor_list = [ 
        ['Alan Alda', 5, 10, 15],
        ['Bob Barker', 1000, 5000],
        ['Cindy Crawford', 75, 250, 600],
        ['David Duchovny', 91],
        ['Emilio Esteves', 70, 70, 70]
        ]

    print u""
    print u"*** Welcome To Mailroom Madness ***"
    print u""
    print u"Menu Options:"
    print u"Type T to send a thank you note"
    print u"Type R to create a report"
    
    # Convert to lower case before validating, so user can input either upper or lower case
    input_string = raw_input('Enter T or R: ').lower()

    # Validate inputs
    while input_string != 't' and input_string != 'r':
        print u"Valid options are T or R: "
        input_string = raw_input().lower()
    print u""

    # Send Thank You Note
    if input_string == 't':
        send_thank_you_note(donor_list)



