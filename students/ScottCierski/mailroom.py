def main_prompt(donor_list):
    """Display main prompt for mailroom program"""

    print u""
    print u"*** Welcome To Mailroom Madness ***"
    print u""
    print u"Menu Options:"
    print u"Type T to send a thank you note"
    print u"Type R to create a report"
    print u"Type Q to quit"

    # Convert to lower case before validating, so user can input either upper or lower case
    input_string = raw_input('Enter T or R or Q: ').lower()

    # Validate inputs
    while input_string not in ('t', 'r', 'q'):
        print u"Valid options are T or R or Q: "
        input_string = raw_input().lower()
    print u""

    # Send Thank You Note
    if input_string == 't':
        send_thank_you_note(donor_list)
    # Create Report
    elif input_string == 'r':
        create_report(donor_list)
    # Quit the program
    elif input_string == 'q':
        print u"Good bye."
    else:
        print u"This should never happen."


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

    # Prompt user for a donation amount for current donor, and add it to that donor's donation history
    input_donation = raw_input("Enter a donation amount for %s: " % input_string)

    #Check to see if input is a number, reprompt if not
    # print type(input_donation)
    # while type(input_donation) != int:
    #     print u"Sorry, we accept whole dollar amounts only."
    #     input_donation = raw_input("Enter a donation amount for %s: " % input_string)

    for a in donor_list:
        if a[0] == input_string:
            a.append(int(input_donation))

    # print donor_list

    # Print thank you email to the console
    print u"Dear %s, thank you for your generous donation of $%s." % (input_string, input_donation)

    # Send user back to main prompt
    main_prompt(donor_list)


def create_report(donor_list):
    """Print list of donors, sorted by total historical donation amount"""
    
    print u"  Name         |  Total Donated  |  # of Donations  |  Average Donation"
    print u"=" * 71
    #Print donor name, sum of donations, # of donations, and average donation amount
    for a in donor_list:
        print a[0], sum(a[1:]), len(a)-1, sum(a[1:]) / len(a)-1

    # Send user back to main prompt
    main_prompt(donor_list)


if __name__ == '__main__':

    # Establish initial donor data, which is a list of lists
    donor_list = [ 
        ['Alan Alda', 5, 10, 15],
        ['Bob Barker', 1000, 5000],
        ['Cindy Crawford', 75, 250, 600],
        ['David Duchovny', 91],
        ['Emilio Esteves', 70, 70, 70]
        ]

    # Send user to main prompt
    main_prompt(donor_list)