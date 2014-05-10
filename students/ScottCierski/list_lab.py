def do_fruit_stuff():
    """Perform various list actions on lists of fruit"""

    # Section 1 of 4
    print u''
    print u"*** Starting Section 1 of 4 ***"
    fruit_list_section_1 = ['Apples', 'Pears', 'Oranges','Peaches']
    print fruit_list_section_1

    new_fruit = raw_input('Please enter a new fruit: ')
    fruit_list_section_1.append(new_fruit)
    print fruit_list_section_1
    
    fruit_number = int(raw_input('Please enter the number of a fruit in the list (valid numbers are 1 through 5): '))
    while fruit_number < 1 or fruit_number > 5:
        fruit_number = int(raw_input('Please enter a number from 1 to 5: '))
    print fruit_list_section_1[fruit_number - 1]
    print u''

    print u"Adding 'Grapes' to the end of the list (using '+')..."
    grapes_list = ['Grapes']
    fruit_list_section_1  = fruit_list_section_1 + grapes_list
    print fruit_list_section_1
    print u''

    print u"Adding 'Plums' to the end of the list (using 'insert')..."
    fruit_list_section_1.insert(len(fruit_list_section_1), 'Plums')
    print fruit_list_section_1
    print u''

    print u'Displaying all fruits beginning with "P"...'
    for fruit in fruit_list_section_1:
        if fruit[:1] =='P':
            print fruit
    print u''

    print 'Printing the current list...'
    print fruit_list_section_1
    print u''

    # Section 2 of 4
    print u"*** Starting Section 2 of 4 ***"
    fruit_list_section_2 = fruit_list_section_1[:]
    print 'Removing the last fruit from the list...'
    fruit_list_section_2.pop()
    print 'Printing the current list...'
    print fruit_list_section_2

    fruit_to_delete = raw_input('Please enter a fruit to delete from the list: ')
    fruit_list_section_2.remove(fruit_to_delete)
    print 'Printing the current list...'
    print fruit_list_section_2
    print u''

    # Section 3 of 4
    print u"*** Starting Section 3 of 4 ***"
    fruit_list_section_3 = fruit_list_section_1[:]
    fruit_list_section_3_copy = fruit_list_section_3[:]
    for fruit in fruit_list_section_3_copy:
        print u"Do you like " + fruit.lower() + u"? Type yes or no: "
        fruit_choice = raw_input()
        fruit_choice = fruit_choice.lower()
        while fruit_choice != 'yes' and fruit_choice != 'no':
            print u"Please type yes or no: "
            fruit_choice = raw_input()
            fruit_choice = fruit_choice.lower()
        if fruit_choice == 'no':
            print u"OK, removing " + fruit + u" from the list."
            fruit_list_section_3.remove(fruit)
            print fruit_list_section_3
        elif fruit_choice == 'yes':
            print u"OK, we'll keep " + fruit + u" in the list."
            print fruit_list_section_3
    print u''

    # Section 4 of 4
    print u"*** Starting Section 4 of 4 ***"
    fruit_list_section_4 = fruit_list_section_1[:]
    fruit_list_section_4_copy = fruit_list_section_4[:]
    
    for fruit in fruit_list_section_4:
        reversed_fruit = fruit[::-1]
        fruit_list_section_4_copy.remove(fruit)
        fruit_list_section_4_copy.append(reversed_fruit)
    
    fruit_list_section_4.pop()
    print fruit_list_section_4
    print fruit_list_section_4_copy

    print u"*** Script Complete ***"

if __name__ == '__main__':
    do_fruit_stuff()