def item_1(d1):
    """Perform various actions on initial dict"""

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

    print u"Creating a dict using the same keys as d1 but with the number of 'a's in each value..."
    a_dict = {}
    for k, v in d1.items():
        a_dict.setdefault(k, v.count('a'))
    print a_dict
    print u""


if __name__ == '__main__':

    # Establish initial dict
    print u"Establishing initial dictionary 'd1'..."
    d1 = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}

    item_1(d1)
    item_2()
    item_3(d1)