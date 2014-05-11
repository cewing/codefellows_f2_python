#!/usr/bin/python


import sys
import copy


# Create fruitlist
fruitlist = [u"Apples", u"Pears", u"Oranges", u"Peaches"]


# Display all fruit  - helper method
def displayAllFruit(fruitlist):
    sys.stdout.write("\nHere is the current list of fruit:\n")
    sys.stdout.write(", ".join(fruitlist))
    sys.stdout.write("\n\n")


# isInt - validate whether user input string is an integer
def isInt(userInput):
    try:
        int(userInput)
        return True
    except ValueError:
        return False


# List Lab - Series 1
def fruitSeriesOne(fruitlist):
    f = copy.copy(fruitlist)
    displayAllFruit(f)
    # User add to end of fruit list
    userInput = raw_input("Name a fruit to add to the end.-->").decode()
    while userInput == "":
            userInput = raw_input("Name a fruit" +
                                  " to add to the end.-->").decode()
    userInput = userInput.capitalize()
    f.append(userInput)
    displayAllFruit(f)
    # User pick a fruit list index to display
    userInput = raw_input("Pick a number between 1 and "
                          + str(len(f)) +
                          " to display the corresponding fruit.-->")
    while isInt(userInput) is False or int(userInput) <= 0 or int(userInput) > len(f):
            userInput = raw_input("Pick a number between 1 and "
                                  + str(len(f)) +
                                  " to display the corresponding fruit.-->")
    sys.stdout.write("\nFruit #" + userInput + ": "
                     + f[int(userInput)-1] + "\n")
    sys.stdout.write("\n")
    # User add to beginning of fruit list using "+"
    userInput = raw_input("Name a fruit to add to the beginning.-->").decode()
    while userInput == "":
            userInput = raw_input("Name a fruit" +
                                  " to add to the beginning.-->").decode()
    userInput = userInput.capitalize()
    f = [userInput] + f
    displayAllFruit(f)
    # User add to beginning of fruit list using insert
    userInput = raw_input("Name a fruit to add to the beginning.-->").decode()
    while userInput == "":
            userInput = raw_input("Name a fruit" +
                                  " to add to the beginning.-->").decode()
    userInput = userInput.capitalize()
    f.insert(0, userInput)
    displayAllFruit(f)
    # Display all fruits in the list that begin with the letter P
    p_fruitlist = []
    sys.stdout.write("Here are the fruits in the current list" +
                     " that start with the letter 'P'?\n"),
    for fruit in f:
        if fruit.startswith('P'):
            p_fruitlist.append(fruit)
    sys.stdout.write(", ".join(p_fruitlist))
    sys.stdout.write("\n\n")


# List Lab - Series 2
def fruitSeriesTwo(fruitlist):
    f = copy.copy(fruitlist)
    displayAllFruit(f)
    # Remove last fruit from fruitlist
    sys.stdout.write("Let's remove the last fruit from the list...\n")
    f.pop()
    displayAllFruit(f)
    # User pick a fruit to delete
    userInput = raw_input("Name a fruit to delete from the list.-->").decode()
    userInput = userInput.capitalize()
    while userInput not in f:
            userInput = raw_input("Name a fruit" +
                                  " to delete from the list.-->").decode()
            userInput = userInput.capitalize()
    f.remove(userInput)
    displayAllFruit(f)


# List Lab - Series 3
def fruitSeriesThree(fruitlist):
    f = copy.copy(fruitlist)
    # User picks fruit to delete one by one
    for fruit in f[:]:
        userInput = raw_input("Do you like " +
                              fruit.lower() + "?-->").decode()
        while userInput != 'no' and userInput != 'yes':
            userInput = raw_input("Do you like " +
                                  fruit.lower() +
                                  "? Please answer 'yes' or 'no'-->").decode()
        if userInput == "no":
                f.remove(fruit)
    displayAllFruit(f)


# List Lab - Series 4
def fruitSeriesFour(fruitlist):
    # Make a copy of the fruitlist & spell each fruit backwards
    reverseSpellList = copy.copy(fruitlist)
    for fruit in fruitlist:
        reverseSpellList.append(fruit[::-1])
        reverseSpellList.remove(fruit)
    sys.stdout.write("Here is the copied list with spelling reversed:\n")
    sys.stdout.write(", ".join(reverseSpellList))
    displayAllFruit(fruitlist)


sys.stdout.write("---------------------Series One----------------------\n")
fruitSeriesOne(fruitlist)
sys.stdout.write("---------------------Series Two ---------------------\n")
fruitSeriesTwo(fruitlist)
sys.stdout.write("---------------------Series Three -------------------\n")
fruitSeriesThree(fruitlist)
sys.stdout.write("---------------------Series Four --------------------\n")
fruitSeriesFour(fruitlist)
