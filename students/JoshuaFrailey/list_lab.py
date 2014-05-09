def _validate_input(prompt, accpet):  # Valid _input or Validate_input?
    u"""Return user input if in accepted value"""
    response = raw_input(prompt)
    while response not in accpet:
        response = raw_input(
            u"""That value was not valid. Please choose from {}: """.format(accpet))
# Find out how to best deal with the length of the above
    return response


def _print_list(list_):
    pass

# Series 1:
fruit_list = [u"Apples", u"Pears", u"Oranges", u"Peaches"]
print fruit_list
user_fruit = raw_input(u'Please enter a fruit to add to the list: ')
fruit_list.append(user_fruit)
user_picks_fruit = _validate_input(
    u"""Please enter a number corresponding to a fruit in the list (starting at 1): """,
    str(range(1, len(fruit_list)))
    )
print u"""You picked fruit number {}, {}""".format(
    user_picks_fruit, fruit_list[int(user_picks_fruit)-1]
    )
fruit_list += [u"Mangos"]
print fruit_list
fruit_list.insert(0, u"Papaya")

for fruit in fruit_list:
    if fruit.startswith(u'P'):
        print fruit
