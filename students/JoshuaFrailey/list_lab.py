#!/usr/bin/env python
def _validate_input(prompt, accept):  # Valid _input or Validate_input?
    u"""Return user input if in accepted string or list of strings"""
    accept_copy = accept[:]
    if isinstance(accept_copy, str):
        accept_copy = accept_copy.lower()
    else:
        for i, ele in enumerate(accept_copy):
            accept_copy[i] = ele.lower()
    response = unicode(raw_input(prompt).lower())
    while response not in accept_copy:
        prompt = u"That value was not valid. "
        prompt += u"Please choose from {} \n--> ".format(accept)
        response = unicode(raw_input(prompt)).lower()
    return response


def _print_basket(list_):
    u"""Print the contents of a 'basket'"""
    if list_:
        print u"The basket contains:",
        for i, ele in enumerate(list_):
            if i == len(list_)-1:
                print ele
            else:
                print ele,
    else:
        print u"The baseket is empty!"

original_fruit_list = [u"Apples", u"Pears", u"Oranges", u"Peaches"]

# Series 1:
fruit_list = original_fruit_list[:]
_print_basket(fruit_list)
prompt = u"Please enter a fruit to add to the basket:\n--> "
user_fruit = unicode(raw_input(prompt))
while True:
    if user_fruit:
        break
    else:
        user_fruit = unicode(raw_input(u"Please enter a fruit\n--> "))
fruit_list.append(user_fruit.title())
_print_basket(fruit_list)
prompt = u"Please enter a number corresponding to a fruit in the list "
prompt += u"(starting at 1={})\n--> "
user_picks_fruit = _validate_input(
    prompt.format(fruit_list[0]), str(range(1, len(fruit_list)+1))
    )
print u"You picked fruit number {}, {}".format(
    user_picks_fruit, fruit_list[int(user_picks_fruit)-1]
    )
print u"Adding Mangos to the front of the basket"
fruit_list = [u"Mangos"] + fruit_list
_print_basket(fruit_list)
print u"Adding Papaya to the front of the basket"
fruit_list.insert(0, u"Papaya")
_print_basket(fruit_list)

print u"Displaying all fruit that start with the letter 'P'"
for fruit in fruit_list:
    if fruit.startswith(u"P"):
        print fruit,
print ""

# Series 2
fruit_list = original_fruit_list[:]
_print_basket(fruit_list)
print u"Removing the last fruit from the basket"
fruit_list.pop()
_print_basket(fruit_list)
prompt = u"Please enter a fruit to remove from the basket.\n--> "
user_fruit = _validate_input(prompt, fruit_list)
fruit_list = fruit_list*2
msg = u"Doubling the fruit in the basket and removing {} ".format(user_fruit)
msg += u"from the basket"
while user_fruit.title() in fruit_list:
    fruit_list.remove(user_fruit.title())
_print_basket(fruit_list)

# Series 3
fruit_list = original_fruit_list[:]
_print_basket(fruit_list)

for fruit in original_fruit_list:
    prompt = u"Do you like {}? ".format(fruit.lower())
    accept = [u"Yes", u"No", u"Y", u"N"]
    user_likes = _validate_input(prompt, accept)
    if user_likes.lower() in [u"no", u"n"]:
        while fruit in fruit_list:
            fruit_list.remove(fruit)
_print_basket(fruit_list)

# Series 4
fruit_list = original_fruit_list[:]

for i, fruit in enumerate(fruit_list):
    fruit_list[i] = fruit[::-1]

original_fruit_list.pop()
_print_basket(original_fruit_list)
_print_basket(fruit_list)
