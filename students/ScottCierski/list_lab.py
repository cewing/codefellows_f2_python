import sys

def do_stuff():
    """doc string"""
    fruit_list = ['Apples', 'Pears', 'Oranges','Peaches']
    print fruit_list
    # new_fruit = raw_input('Please enter a new fruit: ')
    # fruit_list.append(new_fruit)
    # print fruit_list
    # fruit_number = raw_input('Please enter the number of a fruit in the list: ')
    # print fruit_list[int(fruit_number)-1]

    # print 'Adding "Grapes" to the end of the list (using "+")...'
    # grapes_list = ['Grapes']
    # fruit_list  = fruit_list + grapes_list
    # print fruit_list

    # print 'Adding "Plums" to the end of the list (using "insert")...'
    # fruit_list.insert(len(fruit_list), 'Plums')
    # print fruit_list

    # print 'Displaying all fruits beginning with "P"...'
    # for fruit in fruit_list:
    #     if fruit[:1] =='P':
    #         print fruit

    # print 'Printing the current list...'
    # print fruit_list

    # print 'Removing the last fruit from the list...'
    # fruit_list.pop()
    # print 'Printing the current list...'
    # print fruit_list

    # fruit_to_delete = raw_input('Please enter a fruit to delete from the list: ')
    # fruit_list.remove(fruit_to_delete)
    # print 'Printing the current list...'
    # print fruit_list

    fruit_list_copy = fruit_list[:]
    for fruit in fruit_list_copy:
        print "Do you like " + fruit.lower() + "? Type yes or no: "
        fruit_choice = raw_input()
        fruit_choice = fruit_choice.lower()
        while fruit_choice != 'yes' and fruit_choice != 'no':
            print "Please type yes or no: "
            fruit_choice = raw_input()
            fruit_choice = fruit_choice.lower()
        if fruit_choice == 'no':
            print u"OK, removing " + fruit + u" from the list."
            fruit_list.remove(fruit)
            print fruit_list
        elif fruit_choice == 'yes':
            print u"OK, we'll keep " + fruit + " in the list."
            print fruit_list

if __name__ == '__main__':
    do_stuff()