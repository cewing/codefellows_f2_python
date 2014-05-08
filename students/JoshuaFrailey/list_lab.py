fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print fruit_list
user_fruit = raw_input(
    """
    Please enter a number corresponding to a fruit in the list (starting
    at 1):
    """
    )
print str(user_fruit) + str(fruit_list[user_fruit])
fruit_list += ["Mangos"]
print fruit_list
