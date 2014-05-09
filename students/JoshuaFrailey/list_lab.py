def _validate_input(prompt, accpet):  # Valid _input or Validate_input?
    u"""Return user input if in accepted value"""
    response = raw_input(prompt)
    while response not in accpet:
        response = raw_input(
            u"""That value was not valid. Please choose from {}: """.format(accpet))
# Find out how to best deal with the length of the above
    return response


def _print_basket(list_):
    print u"The basket contains:",
    for ele in list_:
        print ele,
    print u"\n"

# Series 1:
fruit_list = [u"Apples", u"Pears", u"Oranges", u"Peaches"]
_print_basket(fruit_list)
# May want to ensure empty string is not added by user
user_fruit = raw_input(u'Please enter a fruit to add to the basket: ')
fruit_list.append(user_fruit)
_print_basket(fruit_list)
user_picks_fruit = _validate_input(
    u"""Please enter a number corresponding to a fruit in the list (starting at 1): """,
    str(range(1, len(fruit_list)+1))
    )
print u"""You picked fruit number {}, {}""".format(
    user_picks_fruit, fruit_list[int(user_picks_fruit)-1]
    )
fruit_list += [u"Mangos"]
_print_basket(fruit_list)
fruit_list.insert(0, u"Papaya")
_print_basket(fruit_list)

# Put in function?
for fruit in fruit_list:
    if fruit.startswith(u'P'):
        print fruit

# Series 2
_print_basket(fruit_list)
fruit_list.pop()
_print_basket(fruit_list)
user_fruit = _validate_input(u"Please enter a fruit to remove from the basket: ", fruit_list)
fruit_list = fruit_list*2
while user_fruit in fruit_list:
    fruit_list.remove(user_fruit)
_print_basket(fruit_list)
