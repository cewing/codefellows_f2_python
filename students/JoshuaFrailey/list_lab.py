def _validate_input(prompt, accpeted_input):  # Valid _input or Validate_input?
    u"""Return True if user input is in accepted value"""
    response = raw_input(prompt)
    while response not in accpeted_input:
        response = raw_input(
            u"""That value was not valid. Please choose from {}: """.format(accpeted_input))
    return True
# fruit_list = [u"Apples", u"Pears", u"Oranges", u"Peaches"]
# print fruit_list
# user_fruit = raw_input(
#     u'Please enter a fruit to add to the list: '
#     )  # Need to verify added fruit is a string
# fruit_list.append(user_fruit)
# user_picks_fruit = raw_input(
#     u"""
#     Please enter a number corresponding to a fruit in the list (starting
#     at 1):
#     """  # fix formatting
#     )
# # Need to convert user_picks_fruit to int and subtract 1
# print str(user_picks_fruit) + str(fruit_list[user_picks_fruit])
# fruit_list += [u"Mangos"]
# print fruit_list
# fruit_list.insert(0, u"Papaya")

# for fruit in fruit_list:
#     if fruit.startswith(u'P'):
#         print fruit
