def item_1(d1):
    """Perform various actions on initial dict"""

    print u"*** Item 1 ***"
    print u""

    print u"Printing initial dict..."
    print d1
    print u""

    print u"Removing 'cake' from d1..."
    d1.pop('cake')
    print d1
    print u""

    print u"Adding 'fruit' : 'Mango' to d1..."
    d1.setdefault('fruit', 'Mango')
    print d1
    print u""

    print u"Here are all the current keys in d1:"
    for k in d1.keys():
        print k
    print u""

    print u"Here are all the current values in d1:"
    for v in d1.values():
        print v
    print u""

    print u"Is 'cake' among the current keys in d1?"
    is_cake_in_d1 = 'cake' in d1.keys()
    print is_cake_in_d1
    print u""

    print u"Is 'Mango' among the current values in d1?"
    is_mango_in_d1 = 'Mango' in d1.values()
    print is_mango_in_d1
    print u""


def item_2():
    """Create dict of integers 0 through 15 and their hex values"""

    print u"*** Item 2 ***"
    print u""

    print u"Creating a dict of integers 0 through 15 and their hex values..."
    int_hex_keys = []
    int_hex_values = []
    for i in range(16):
        int_hex_keys.append(i)
        int_hex_values.append(hex(i))
    z1 = dict(zip(int_hex_keys, int_hex_values))
    print z1
    print u""


def item_3(d1):
    """Create dict using same keys as d1 but with number of 'a's in each value"""

    print u"*** Item 3 ***"
    print u""

    print u"Creating a dict using the same keys as d1 but with the number of 'a's in each value..."
    a_dict = {}
    for k, v in d1.items():
        a_dict.setdefault(k, v.count('a'))
    print a_dict
    print u""


def item_4():
    """Create sets that contain numbers from zero through twenty, divisible 2, 3 and 4"""

    print u"*** Item 4 ***"
    print u""

    s2 = set()
    for i in range(21):
        if i % 2 == 0:
            s2.add(i)
    print u"Printing s2..."
    print s2
    print u""

    print u"Printing s3..."
    s3 = set()
    for i in range(21):
        if i % 3 == 0:
            s3.add(i)
    print s3
    print u""

    print u"Printing s4..."
    s4 = set()
    for i in range(21):
        if i % 4 == 0:
            s4.add(i)
    print s4
    print u""

    print u"Is s3 a subset of s2?"
    print s3.issubset(s2)
    print u""

    print u"Is s4 a subset of s2?"
    print s4.issubset(s2)
    print u""


def item_5():
    """Create a set and a frozenset and performs actions with them"""

    print u"*** Item 5 ***"
    print u""

    item_5_set = set()
    item_5_string_1 = 'Python'
    item_5_frozenset = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))

    for c in "".join(item_5_string_1):
        item_5_set.add(c)
        item_5_set.add('i')

    print u"Printing set..."
    print item_5_set
    print u""

    print u"Printing frozenset..."
    print item_5_frozenset
    print u""

    print u"Printing union..."
    print item_5_set.union(item_5_frozenset)
    print u""

    print u"Printing intersection..."
    print item_5_set.intersection(item_5_frozenset)
    print u""

if __name__ == '__main__':

    # Establish initial dict
    print u""
    print u"Establishing initial dictionary 'd1'..."
    d1 = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}
    print u""

    # Run all the functions
    item_1(d1)
    item_2()
    item_3(d1)
    item_4()
    item_5()

    print u"End of script."