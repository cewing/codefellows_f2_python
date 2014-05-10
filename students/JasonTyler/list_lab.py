"""Task 1, List Lab"""

def get_input():
    """Get user input"""
    text_in = raw_input(u">>> ")
    return text_in


def within_list_index(raw_in, lst):
    """Validate that user input is integer within shifted list index"""
    try:
        int(raw_in)
    except ValueError:
        return False
    else:
        # using index starting with 1 convention, not 0
        if 0 < int(raw_in) <= len(lst):
            return True
        else:
            return False 


def display_list():
    """Display fruit list"""
    print u"Here are some yummy fruits:", fruit_list


def list_rm(val, lst):
    """Remove an item of value == val from lst and return status."""
    try:
        lst.remove(val)
    except ValueError:
        return False
    else:
        return True
     

def list_rm_all(val, lst):
    """Remove all items of value = val from lst and return status."""
    # Tesing whether any item of val exists
    exists_flag = list_rm(val, lst)
    # Use False return to indicate that no item was removed
    if not exists_flag: return False
    else:
        while exists_flag:
            exists_flag = list_rm(val, lst)
        return True

# Start of interactive prompt, "Series 1"
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
display_list()

print u"Would you like to add another?"
nother_fruit = get_input()
fruit_list.append(str(nother_fruit))
display_list()

print u"Which fruit number would you like to display?"
while True:
    fruit_number = get_input()
    if within_list_index(fruit_number, fruit_list):
        print u"Here's some %s." % fruit_list[int(fruit_number) - 1]
        break
    else:
        print u"The fruits are ordered. Which number?"

print u"Would you like to add another fruit?"
nother_fruit = get_input()
fruit_list = [nother_fruit] + fruit_list
display_list()

print u"Would you like to add another fruit?"
nother_fruit = get_input()
fruit_list.insert(0 ,nother_fruit)
display_list()

print u"Here are all fruits beginning with a 'P':"
found_p = False
for fruit in fruit_list:
    if fruit[0].lower() == 'p': 
        print fruit
        found_p = True
    else: pass
else:
    if not found_p:
        print u"Sorry, I didn't actually see any 'P' fruits..."
    else: pass

# Start of remove methods, calling this "Series 2"
display_list()
fruit_list.pop()

fruit_remove_flag = False
while not fruit_remove_flag:
    fruit_list *= 2 
    display_list()
    print "Which fruit would you like to remove?"
    fruit_to_rm = get_input()
    fruit_remove_flag = list_rm_all(fruit_to_rm, fruit_list)

display_list()

