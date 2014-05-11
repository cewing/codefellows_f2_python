# Usage Notes
# Report formatting is designed for consoles with fixed length fonts


def main_prompt(donor_list):
    """Display main prompt for mailroom program"""

    print u""
    print u"*** Welcome To Mailroom Madness ***"
    print u""
    menu_options_header = u"Menu Options:"
    print menu_options_header
    print u"-" * len(menu_options_header)
    print u"Type T to send a thank you note"
    print u"Type R to create a report"
    print u"Type Q to quit"

    # Convert to lower case before validating, so user can input either upper or lower case
    input_string = raw_input('Enter T or R or Q: ').lower()

    # Validate inputs
    while input_string not in ('t', 'r', 'q'):
        input_string = raw_input("Valid options are T or R or Q: ").lower()
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

    thank_you_note_options_header = u"Thank You Note Options:"
    enter_current_donor_string = u"Type the full name of a current donor"
    enter_new_donor_string = u"To add a new donor, type the new donor's name"
    type_list_string = u"Type 'list' for a list of donors"
    type_q_string = "Type Q to quit to main prompt"

    print thank_you_note_options_header
    print u"-" * len(thank_you_note_options_header)
    print enter_current_donor_string
    print enter_new_donor_string
    print type_list_string
    print type_q_string
    input_string = raw_input("Please make your selection: ")

    # Print just the donor names, then reprompt user for a name
    while input_string == 'list':
        for a in donor_list:
            print a[0]

        print u""
        print thank_you_note_options_header
        print u"-" * len(thank_you_note_options_header)
        print enter_current_donor_string
        print enter_new_donor_string
        print type_list_string
        print type_q_string
        input_string = raw_input("Please make your selection: ")

    if input_string.lower() == 'q':
        main_prompt(donor_list)
        return
    else:
        # Create a new list just of donor names
        donor_list_names = []
        for a in donor_list:
            donor_list_names.append(a[0])

        # If donor not already in list, set a flag
        # Do not add the donor yet, since the user may elect to quit before also adding a donation
        is_new_donor = False;
        if input_string not in donor_list_names:
            is_new_donor = True;

        # Prompt user for a donation amount, and add it to that donor's donation history
        donation_options_header_string = u"Donation Options"
        print u""
        print donation_options_header_string
        print u"-" * len(donation_options_header_string)
        print u"Enter a donation amount for %s: " % input_string
        print type_q_string
        input_donation = raw_input("Please make your selection: ")

        if input_donation.lower() == 'q':
            main_prompt(donor_list)
            return
        else:

            #Check to see if input is a number, reprompt if not
            while unicode(input_donation).isnumeric() != True:
                print u"Sorry, donation amount must be a number."
                print u""
                print donation_options_header_string
                print u"-" * len(donation_options_header_string)
                print u"Enter a donation amount for %s: " % input_string
                print type_q_string
                input_donation = raw_input("Please make your selection: ")

            # If the donor is new, add the new donor to the list
            if is_new_donor == True:
                print u"Adding %s to donor list." % input_string
                donor_list.append([input_string])

            for a in donor_list:
                if a[0] == input_string:
                    a.append(int(input_donation))
                    print u"Adding donation of %s for donor %s." % (input_donation, input_string)

            # print donor_list

            # Print thank you email to the console
            print u"Dear %s, thank you for your generous donation of $%s." % (input_string, input_donation)

    # Send user back to main prompt
    main_prompt(donor_list)


def create_report(donor_list):
    """Print list of donors, sorted by total historical donation amount"""
    
    # Print report header
    print u"  Name         |  Total Donated  |  # of Donations  |  Average Donation"
    print u"=" * 71
    
    # Get or calculate donor name, sum of donations, # of donations, and average donation amount
    for a in donor_list:
        donor_name = a[0]
        donor_sum = sum(a[1:])
        number_of_donations = len(a)-1
        average_donation = donor_sum / number_of_donations

        # Calculate spacing between values for report formatting
        space_1 = u" " * (30 - (len(donor_name) + len(str(donor_sum))))
        space_2 = u" " * (45 - (len(donor_name) + len(space_1) + len(str(donor_sum))))
        space_3 = u" " * (64 - (len(donor_name) + len(space_1) + len(str(donor_sum)) + \
            len(space_2) + len(str(number_of_donations)) + len(str(average_donation))))

        # Print everything
        print donor_name, space_1, donor_sum, space_2, number_of_donations, space_3, average_donation
        print u"-" * 71

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