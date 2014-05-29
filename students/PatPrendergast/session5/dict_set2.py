#dict_set2.py - adding comprehensions homework


def setmaker(n, outer):
  ''' Produces a set of numbers divisible by n within a range. 

  n is the divisor for modulo each number in the outer range'''
    
  return {e for e in range(outer) if e % n == 0}
    

preferences = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

print u'Preferences: ', preferences

print u"""{name} from {city} loves:
          {cake} cake  
          {fruit} 
          {salad} salad 
          {pasta}.""".format(
            name=preferences[u'name'],
            city=preferences[u'city'], 
            cake=preferences[u'cake'], 
            fruit=preferences[u'fruit'],
            salad=preferences[u'salad'],
            pasta=preferences[u'pasta'])
print ''
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

the_keys = [num for num in range(16)]
print 'THE KEYS: ',  the_keys
# the_keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
the_values_string = u"0123456789ABCDEF"
the_values = [e for e in the_values_string]
print U'THE VALUES :', the_values
#the_values = [u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'A', u'B', u'C', u'D', u'E', u'F']
hexadecimals = {k: v for k, v in zip(the_keys, the_values)}
print "Hexadecimals: ", hexadecimals

print "____________"
print ""

counting_a = dict((key, value.count('a')) for key, value in preferences.items())
print "A_Count Dictionary (number of a's in values): ", counting_a

print "____________"
print ""


s2 = setmaker(2, 20)
s3 = setmaker(3, 20)
s4 = setmaker(4, 20)
the_fives = setmaker(5, 500)

print u'S2: ',s2
print u'S3: ',s3
print u'S4: ',s4
print u'Also fives in 500: ', the_fives

print u'Is S3 a subset of S2? ', s3.issubset(s2)
print u'Is S4 a subset of S2? ', s4.issubset(s2)

py_string = u'Python'
py = {let for let in py_string}
#py = set([u'P', u'y', u't', u'h', u'o', u'n'])
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

