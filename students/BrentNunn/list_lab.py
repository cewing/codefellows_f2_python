#!/usr/bin/env python

fruits = [u"Apples", u"Pears", u"Oranges", u"Peaches"]

def print_fruits(fruits):
    """Print all fruits in the sequence"""
    for fruit in fruits:
        print fruit,    

    print ""

def get_fruit(prompt):
    """Get the name of another fruit."""
    while True:
        fruit_in = raw_input(prompt)
        if fruit_in.isalpha():
            break
        else:
            print(u"Letters only please.")

    return unicode(fruit_in)

def get_num(max_num):
    """Get a number in the range of 1 to passed parameter"""
    while True:
        num_in = raw_input(u"\nEnter a number between 1 and {}: ".format(max_num))
        if num_in.isdigit():
            num_in = int(num_in)
            if num_in >= 1 and num_in <= max_num:
                break
            else:
                print u"Please limit your entry to the range specified."
        else:
            print u"Numbers only please."

    return num_in

def series_1(fruits):
    """\nlist_lab series 1, creating a list of fruits"""
    print u"list_lab series 1"

    print_fruits(fruits)
    fruits.extend([get_fruit(u"\nPlease add another fruit to the list: ")])
    print_fruits(fruits)

    fruit_num = get_num(len(fruits))
    print u"Fruit number {} is {}.".format(fruit_num, fruits[fruit_num - 1])

    one_fruit = [get_fruit(u"\nPlease add another fruit to the list: ")]
    fruits = one_fruit + fruits
    print_fruits(fruits)

    one_fruit = get_fruit(u"\nPlease add another fruit to the list: ")
    fruits.insert(0, one_fruit)
    print_fruits(fruits)

    print u"\nThese fruits begin with 'P':"
    for fruit in fruits:
        if fruit[0] == 'P' or fruit[0] == 'p':
            print fruit

    return fruits

def series_2(fruits):
    """list_lab series 2, deleting items from the list of fruits"""
    print u"\nlist_lab series 2"

    fruits2 = fruits[:]
    print_fruits(fruits2)

    print u"\nRemoving last item from fruits"
    fruits2.pop()
    print_fruits(fruits2)

    print u"\nDoubling the series 2 list"
    fruits2 *= 2
    print_fruits(fruits2)

    delete_fruit = get_fruit(u"\nEnter fruit to delete from the list: ")
    new_fruits = []
    while True:
        for fruit in fruits2:
            if fruit <> delete_fruit:
                new_fruits += [fruit]

        if len(new_fruits) < len(fruits2):
            break
        else:
            delete_fruit = get_fruit(u"Entry not found.  Try again: ")
            new_fruits = []

    print_fruits(new_fruits)

def yes_or_no(prompt):
    while True:
        response = raw_input(prompt)
        if response.isalpha():
            response = response.lower()
            if response == u"yes" or response == u"no":
                return response
            else:
                prompt = u"'yes' or 'no': "


def series_3(fruits):
    """list_lab series 3, determine liked fruits"""
    print u"\nlist_lab series 3"

    fruits3 = fruits[:]
    print_fruits(fruits3)

    liked_fruits = []
    for fruit in fruits3:
        prompt = u"Do you like {}? ".format(fruit.lower())
        liked = yes_or_no(prompt)
        if liked == u"yes":
            liked_fruits += [fruit]

    print_fruits(liked_fruits)

def series_4(fruits):
    """list_lab series 4, copy list and reverse letters"""
    print u"\nlist_lab series 4"

    fruits_reversed = fruits[:]
    print_fruits(fruits)

    for i, fruit in enumerate(fruits_reversed):
        fruits_reversed[i] = fruit[::-1]

    fruits.pop()
    print_fruits(fruits)
    print_fruits(fruits_reversed)

# This assignment has 4 sections, or series of actions based on lists
# list_lab series 1, creating a list of fruits
fruits = series_1(fruits)

# list_lab series 2, remove fruits from the list
series_2(fruits)

# list_lab series 3, create a list of fruits the user likes
series_3(fruits)

# list_lab series 4, copy the list and reverse letters in each fruit
series_4(fruits)