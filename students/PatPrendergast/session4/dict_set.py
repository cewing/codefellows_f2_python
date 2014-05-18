#dict_set.py

def setmaker(n, outer):
    ''' Produces a set of numbers divisible by n within a range. 

    n is the divisor for modulo each number in the outer range'''
    a_list = []
    for e in range(outer):
        if e % n == 0:
            a_list.append(e)
    return set(a_list)


preferences = {u'name': u'Chris', u'city': u'Seattle', u'cake': u'chocolate'}

print u'Preferences: ', preferences

preferences.pop(u'cake')

print u'Preferences: ', preferences

preferences[u'fruit'] = u'Mango'

print u'Preferences: ', preferences
print "____________"
print ""

print u'The Keys: ', preferences.keys()
print u'The Values: ', preferences.values()
print u'Is cake there? ', 'cake' in preferences
print preferences.setdefault('fruit', 'Mango'), "is there."

print u'Preferences: ', preferences
print "____________"
print ""

print u'New Dictionary of Numbers Keys to Hexadecimal Values '


the_keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
the_values = [u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'A', u'B', u'C', u'D', u'E', u'F']

numbers = zip(the_keys, the_values)
hexa_numbers = dict(numbers)
print hexa_numbers
counting_a = dict((key, value.count('a')) for key, value in preferences.items())
print "A_Count Dictionary (number of a's in values): ", counting_a

print "____________"
print ""


s2 = setmaker(2, 20)
s3 = setmaker(3, 20)
s4 = setmaker(4, 20)

print u'S2: ',s2
print u'S3: ',s3
print u'S4: ',s4

print u'Is S3 a subset of S2? ', s3.issubset(s2)
print u'Is S4 a subset of S2? ', s4.issubset(s2)

py = set([u'P', u'y', u't', u'h', u'o', u'n'])
#py.add('i')
print u'Python Set: ', py
an_i = set([u'i'])
py_i = py | an_i
print u'Python Set with i: ', py_i

print "____________"
print ""

marathon = frozenset([u'm', u'a', u'r', u'a', u't', u'h', u'o', u'n'])
print u"Frozen Marathon: ", marathon

print u"Union of Python and Marathon: ",  py.union(marathon)
print u"Intersection of Python and Marathon: ", py.intersection(marathon)
print u'Weird'

print "____________"
print ""

