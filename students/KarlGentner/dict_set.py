#!/usr/bin/python


# Displays the current dictionary
def displayDict(dictionary):
    print u"\nCURRENT DICTIONARY:"
    for key, value in dictionary.iteritems():
        print("{key} : {value}").format(key=key, value=value)


# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
d = {u'name': u'Chris', u'city': u'Seattle', u'cake': u'Chocolate'}
displayDict(d)


# Delete the entry for “cake”.
print u"\nNow let's remove the 'cake' entry"
d.pop(u'cake')
displayDict(d)


# Add an entry for “fruit” with “Mango” and display the dictionary.
print u"\nNow let's add a 'fruit' entry of 'Mango'"
d['fruit'] = 'Mango'
displayDict(d)


# Display the dictionary keys.
print u"\nCURRENT KEYS:"
for key in d.iterkeys():
        print(key)


# Display the dictionary values.
print u"\nCURRENT VALUES:"
for value in d.itervalues():
        print(value)


# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
if u'cake' in d:
    print u"\nTrue: 'cake' is a key in the current dictionary"
else:
    print u"\nFalse: 'cake' is NOT a key in the current dictionary"


# Display whether or not “Mango” is a value in the dictionary.
# Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).
# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘a’s in each value.
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
# Display the sets.
# Display if s3 is a subset of s2 (False)
# and if s4 is a subset of s2 (True).
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
# Create a frozenset with the letters in ‘marathon’
# display the union and intersection of the two sets.