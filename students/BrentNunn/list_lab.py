#!/usr/bin/env python

fruits = [u"Apples", u"Pears", u"Oranges", u"Peaches"]

def print_fruits(fruits):
    for fruit in fruits:
        print fruit    

def get_fruit(prompt):
    fruit_in = None

    while not fruit_in:
        fruit_in = raw_input(prompt)
        if fruit_in.isalpha():
            break
        else:
            print(u"Letters only please.")
            fruit_in = None

    return fruit_in

def get_num(max_num):
    num_in = None

    while not num_in:
        num_in = raw_input(u"Enter a number between 1 and {}: ".format(max_num))
        if num_in.isdigit():
            num_in = int(num_in)
            if num_in >= 1 and num_in <= max_num:
                break
            else:
                print u"Please limit your entry to the range specified."
                num_in = None
        else:
            print u"Numbers only please."
            num_in = None

    return int(num_in)


print_fruits(fruits)
fruits.extend([get_fruit(u"Please add another fruit to the list: ")])
print_fruits(fruits)

fruit_num = get_num(len(fruits))
