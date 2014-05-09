def _validate_input(prompt, accept):  # Valid _input or Validate_input?
    u"""Return user input if in accepted string or list of strings"""
    accept_copy = accept[:]
    if isinstance(accept_copy, str):
        accept_copy = accept_copy.lower()
    else:
        for i, ele in enumerate(accept_copy):
            accept_copy[i] = ele.lower()
    response = raw_input(prompt).lower()
    while response not in accept_copy:
        response = raw_input(
            u"""That value was not valid. Please choose from {}: """.format(accept))
# Find out how to best deal with the length of the above
    return response


def _print_basket(list_):
    print u"The basket contains:",
    for i, ele in enumerate(list_):
        if i == len(list_)-1:
            print ele
        else:
            print ele,


# Series 1:
fruit_list = [u"Apples", u"Pears", u"Oranges", u"Peaches"]
_print_basket(fruit_list)
# May want to ensure empty string is not added by user
user_fruit = raw_input(u'Please enter a fruit to add to the basket: ')
fruit_list.append(user_fruit.title())
_print_basket(fruit_list)
user_picks_fruit = _validate_input(
    u"""Please enter a number corresponding to a fruit in the list (starting at 1 = {}): """.format(fruit_list[0]),
    str(range(1, len(fruit_list)+1))
    )
print u"""You picked fruit number {}, {}""".format(
    user_picks_fruit, fruit_list[int(user_picks_fruit)-1]
    )
print u"Adding Mangos to the basket"
fruit_list += [u"Mangos"]
_print_basket(fruit_list)
print u"Adding Papaya to the basket"
fruit_list.insert(0, u"Papaya")
_print_basket(fruit_list)
original_fruit_list = fruit_list[:]

# Put in function?
print u"Displaying all fruit that start with the letter 'P'"
for i, fruit in enumerate(fruit_list):
    if fruit.startswith(u'P'):
        print fruit,
print ''

# Series 2
_print_basket(fruit_list)
print u"Removing the last fruit from the basket"
fruit_list.pop()
_print_basket(fruit_list)
user_fruit = _validate_input(u"Please enter a fruit to remove from the basket: ", fruit_list)
fruit_list = fruit_list*2
print u"""Doubling the fruit in the basket and removing all {} from the basket""".format(user_fruit)
while user_fruit.title() in fruit_list:
    fruit_list.remove(user_fruit.title())
_print_basket(fruit_list)

# Series 3
series3_fruit_list = original_fruit_list[:]
_print_basket(series3_fruit_list)

for fruit in original_fruit_list:
    user_likes = _validate_input(u"Do you like {}? ".format(fruit.lower()), ["Yes", "No","Y","N"])
    if user_likes == u"No" or user_likes == u"N":
        while user_fruit in series3_fruit_list:
            series3_fruit_list.remove(fruit)

_print_basket(series3_fruit_list)

# Series 4
series4_fruit_list = original_fruit_list[:]

for i, fruit in enumerate(series4_fruit_list):
    series4_fruit_list[i] = fruit[::-1]

original_fruit_list.pop()
_print_basket(original_fruit_list)
_print_basket(series4_fruit_list)
