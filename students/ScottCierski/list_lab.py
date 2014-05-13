def do_fruit_stuff():
    """Perform various list actions on lists of fruit"""

    # Section 1 of 4
    print u""
    print u"*** Starting Section 1 of 4 ***"
    print u""

    print u"Printing current list..."
    fruit_list_section_1 = ['Apples', 'Pears', 'Oranges','Peaches']
    print fruit_list_section_1
    print u""

    new_fruit = raw_input('Please enter a new fruit: ')
    # Convert input to string in case it's not already, and capitalize first character
    new_fruit = str(new_fruit)
    new_fruit = new_fruit[:1].upper() + new_fruit[1:].lower()

    fruit_list_section_1.append(new_fruit)
    print fruit_list_section_1
    print u""
    
    fruit_number = int(raw_input('Please enter the number of a fruit in the list (valid numbers are 1 through 5): '))

    # Validate user input
    while fruit_number < 1 or fruit_number > 5:
        fruit_number = int(raw_input('Please enter a number from 1 to 5: '))

    print u""
    print u"Printing fruit at position " + str(fruit_number) + u"..."
    print fruit_list_section_1[fruit_number - 1]
    print u""

    print u"Adding 'Grapes' to the end of the list (using '+')..."
    grapes_list = ['Grapes']
    fruit_list_section_1  = fruit_list_section_1 + grapes_list
    print fruit_list_section_1
    print u""

    print u"Adding 'Plums' to the end of the list (using 'insert')..."
    fruit_list_section_1.insert(len(fruit_list_section_1), 'Plums')
    print fruit_list_section_1
    print u""

    print u'Displaying all fruits that begin with "P"...'
    for fruit in fruit_list_section_1:
        if fruit[:1] =='P':
            print fruit
    print u""

    print 'Printing the current list...'
    print fruit_list_section_1
    print u""

    # Section 2 of 4
    print u"*** Starting Section 2 of 4 ***"
    print u""

    print u"Printing the list from Section 1..."
    print fruit_list_section_1
    print u""

    # Make a copy of the list from Section 1 for use with Section 2
    fruit_list_section_2 = fruit_list_section_1[:]

    print 'Removing the last fruit from the list...'
    fruit_list_section_2.pop()
    print u""
    print 'Printing the current list...'
    print fruit_list_section_2
    print u""

    fruit_to_delete = raw_input('Please enter a fruit to delete from the list: ')

    # Validate user input
    while fruit_to_delete not in fruit_list_section_2:
        print u""
        print u"That is not in the list, try again."
        print fruit_list_section_2
        fruit_to_delete = raw_input('Please enter a fruit to delete from the list: ')

    fruit_list_section_2.remove(fruit_to_delete)
    print u""
    print 'Printing the current list...'
    print fruit_list_section_2
    print u""

    # Section 3 of 4
    print u"*** Starting Section 3 of 4 ***"
    print u""

    print u"Printing the list from Section 1..."
    print fruit_list_section_1
    print u""

    # Make a copy of the list from Section 1 for use with Section 3
    fruit_list_section_3 = fruit_list_section_1[:]

    # Make a copy of fruit_list_section_3, so we can iterate on the original list and modify the copy
    fruit_list_section_3_copy = fruit_list_section_3[:]

    for fruit in fruit_list_section_3_copy:
        print u"Do you like " + fruit.lower() + u"? Type yes or no: "
        fruit_choice = raw_input()
        fruit_choice = fruit_choice.lower()

        # Validate user input
        while fruit_choice != 'yes' and fruit_choice != 'no':
            print u"Please type yes or no: "
            fruit_choice = raw_input()
            fruit_choice = fruit_choice.lower()

        if fruit_choice == 'no':
            print u"OK, removing " + fruit + u" from the list."
            print u""
            fruit_list_section_3.remove(fruit)
            print fruit_list_section_3
        elif fruit_choice == 'yes':
            print u"OK, we'll keep " + fruit + u" in the list."
            print u""
            print fruit_list_section_3
    print u""

    # Section 4 of 4
    print u"*** Starting Section 4 of 4 ***"
    print u""

    print u"Printing the list from Section 1..."
    print fruit_list_section_1
    print u""

    # Make a copy of the list from Section 1 for use with Section 4
    fruit_list_section_4 = fruit_list_section_1[:]

    # Make a copy of fruit_list_section_4, so we can iterate on the original list and modify the copy
    fruit_list_section_4_copy = fruit_list_section_4[:]
    
    # Iterate through list, remove each item then append that item with its characters reversed
    for fruit in fruit_list_section_4:
        reversed_fruit = fruit[::-1]
        fruit_list_section_4_copy.remove(fruit)
        fruit_list_section_4_copy.append(reversed_fruit)
    
    # Remove last item from our original Section 4 list
    fruit_list_section_4.pop()

    print u"Printing list with last item removed..."
    print fruit_list_section_4
    print u""

    print u"Printing list with characters in each item reversed..."
    print fruit_list_section_4_copy
    print u""

    print u"*** Script Complete ***"
    print u""

if __name__ == '__main__':
    do_fruit_stuff()