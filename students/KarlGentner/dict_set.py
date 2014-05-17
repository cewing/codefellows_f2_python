#!/usr/bin/python


# Displays the current dictionary
def displayDict(a_dict):
    for key, value in a_dict.iteritems():
        print(u"{key} : {value}").format(key=key, value=value)


# Displays the current set
def displaySet(a_set):
    for x in a_set:
        print x,


# Create a dictionary containing:
# “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
d = {u'name': u'Chris', u'city': u'Seattle', u'cake': u'Chocolate'}
print u"\nDictionary 'd':"
displayDict(d)


# Delete the entry for “cake”.
print u"\nDictionary 'd' with the 'cake' entry removed:"
d.pop(u'cake')
displayDict(d)


# Add an entry for “fruit” with “Mango” and display the dictionary.
print u"\nDictionary 'd' with added 'fruit' entry of 'Mango':"
d[u'fruit'] = u'Mango'
displayDict(d)


# Display the dictionary keys.
print u"\nCurrent keys of dictionary 'd':"
for key in d.iterkeys():
        print(key)


# Display the dictionary values.
print u"\nCurrent values of dictionary 'd':"
for value in d.itervalues():
        print(value)


# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
if u'cake' in d:
    print u"\n'cake' is a key in dictionary 'd'."
else:
    print u"\n'cake' is NOT a key in dictionary 'd'."


# Display whether or not “Mango” is a value in the dictionary.
if u'Mango' in d.values():
    print u"\n'Mango' is a value in dictionary 'd'."
else:
    print u"\n'Mango' is NOT a value in dictionary 'd'."


# Using the dict constructor and zip, build a dictionary of numbers
# from zero to fifteen and the hexadecimal equivalent (string is fine).
nums = range(16)
hexnums = []
for x in nums:
    hexnums.append(hex(x))
z = dict(zip(nums, hexnums))
print u"\nDictionary 'z' with keys 0 to 15 and hexadecimal equivalent values:"
displayDict(z)


# Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of ‘a’s in each value.
e = {}
for key, value in d.iteritems():
    e[key] = value.count(u'a')
# OR with a dict expression...
e = {key: value.count(u'a') for key, value in d.iteritems()}
print (u"\nDictionary 'e' : a copy of dictionary 'd' " +
       "with the number of a's in each value:")
displayDict(e)


# Create and displaysets s2, s3 and s4 that contain numbers
# from zero through twenty, divisible 2, 3 and 4.
s2 = set()
for i in range(21):
    if i % 2 == 0:
        s2.add(i)

print u"\n\nSet s2 with numbers 0 though 20 that are divisible by 2:"
displaySet(s2)

s3 = set()
for i in range(21):
    if i % 3 == 0:
        s3.add(i)

print u"\n\nSet s3 with numbers 0 though 20 that are divisible by 3:"
displaySet(s3)

s4 = set()
for i in range(21):
    if i % 4 == 0:
        s4.add(i)

print u"\n\nSet s4 with numbers 0 though 20 that are divisible by 4:"
displaySet(s4)


# Display if s3 is a subset of s2 (False)
if s3.issubset(s2):
    print u"\n\ns3 is a subset of s2."
else:
    print u"\n\ns3 is NOT a subset of s2"


# and if s4 is a subset of s2 (True).
if s4.issubset(s2):
    print u"\n\ns4 is a subset of s2."
else:
    print u"\n\ns4 is NOT a subset of s2"


# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
s = set(u'Python')
s.add(u'i')
print u"\n\nSet 's' with letters in 'Python' and the letter 'i':"
displaySet(s)


# Create a frozenset with the letters in ‘marathon’
fs = frozenset(u'marathon')
print u"\n\nFrozen set 'fs' with letters in 'marathon':"
displaySet(fs)


# display the union and intersection of the two sets.
u = s.union(fs)
print u"\n\nThe union of set 's' and frozen set 'fs':"
displaySet(u)
i = fs.intersection(s)
print u"\n\nThe intersection of set 's' and frozen set 'fs':"
displaySet(i)
