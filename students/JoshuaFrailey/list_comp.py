feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]

# What is the output of:

# >>> comprehension[0]
# 'Lambs'

# >>> comprehension[2]
# 'Orangutans'

feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

# What is the output of:

# >>> len(feast)
# 5

# >>> len(comprehension)
# 3

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [skit * number for number, skit in list_of_tuples]

# >>> comprehension[0]
# 'lumberjack'

# >>> len(comprehension[2])
# 'spamspamspamspam'

list_of_eggs = ['poached egg', 'fried egg']
list_of_meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = ['{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]

# What is the output of:

# >>> len(comprehension)
# 6

# >>> comprehension[0]
# 'poached egg and lite spam'

comprehension = { x for x in 'aabbbcccc'}

# What is the output of:

# >>> comprehension
# {'a', 'b', 'c'}

dict_of_weapons = {
    'first': 'fear', 'second': 'surprise',
    'third': 'ruthless efficiency', 'forth': 'fanatical devotion',
    'fifth': None
    }

dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}

# What is the output of:

# >>> 'first' in dict_comprehension
# False

# >>> 'FIRST' in dict_comprehension
# True

# >>> len(dict_of_weapons)
# 5

# >>> len(dict_comprehension)
# 4


def count_evens(nums):
    return len([num for num in nums if num % 2 == 0])