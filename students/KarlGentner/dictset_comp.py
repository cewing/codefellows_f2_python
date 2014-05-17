#!/usr/bin/python


# Displays the given dictionary
def displayDict(a_dict):
    for key, value in a_dict.iteritems():
        print(u"{key} : {value}").format(key=key, value=value)


# Displays the given dictionary wth particular formatting
def displayDictFormat(a_dict):
    d = a_dict.copy()
    print (u"{name} is from").format(name=d.pop('name')),
    print (u"{city} and likes").format(city=d.pop('city')),
    comma = False
    for key, value in d.iteritems():
        if comma is True:
            print u",",
        print (u"{value} {key}").format(key=key, value=value),
        comma = True
    print u"\n",


# Displays the given set
def displaySet(a_set):
    for x in a_set:
        print x,


# Displays given list of sets
def displayListSet(list):
    for x in range(len(list)):
        print list[x]


# construct dictionary
food_prefs = {u"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}


# 1. Print the dict by passing it to a string format method,
print u"\nDictionary 'food_prefs':"
displayDictFormat(food_prefs)

# 2.  Using a list comprehension, build a dictionary of numbers
# from zero to fifteen and the hexadecimal equivalent (string is fine).
hexnums = [hex(x) for x in range(16)]
z = dict(zip(range(16), hexnums))

print u"\nDictionary 'z' with keys 0 to 15 and hexadecimal equivalent values:"
displayDict(z)

# 3. Previous dict with a dict comprehension
z = {i: hex(x) for x in range(16) for i in range(16)}

print (u"\nOne liner- Dictionary 'z' with keys 0 to 15" +
       "and hexadecimal equivalent values:")
displayDict(z)


# 4. Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of ‘a’s in each value. You can do this either
# by editing the dict in place, or making a new one.
# If you edit in place, make a copy first!
e = {key: value.count('a') for key, value in food_prefs.iteritems()}
print (u"\nDictionary 'e' : a copy of dictionary 'food_prefs'" +
       "with the number of a's in each value:")
displayDict(e)


# 5. Create sets s2, s3 and s4 that contain numbers
# from zero through twenty, divisible 2, 3 and 4.
# 5-1. Do this with one set comprehension for each set.
# (Oops ... I already did this for the original dict set lab.)
s2 = {i for i in range(21) if i % 2 == 0}
s3 = {i for i in range(21) if i % 3 == 0}
s4 = {i for i in range(21) if i % 4 == 0}

print u"\n\nSet s2:"
displaySet(s2)
print u"\n\nSet s3:"
displaySet(s3)
print u"\n\nSet s4:"
displaySet(s4)


# 5-2. What if you had a lot more than 3? – Don’t Repeat Yourself (DRY)
# 5-2-i. create a sequence that holds all three sets
# 5-2-ii. loop through that sequence to build the sets up .
lsthree = [{}, {}, {}]
for x in range(len(lsthree)):
    lsthree[x] = {i for i in range(21) if i % (x+2) == 0}

print u"\n\nList with sets s2, s3, and s4:"
displayListSet(lsthree)


# 5c Extra credit: do it all as a one-liner by nesting a set comprehension
# inside a list comprehension. (OK, that may be getting carried away!)
lsthree = [{i for i in range(21) if i % (x+2) == 0} for x in range(3)]

print u"\n\nOne liner - List with sets s2, s3, and s4:"
displayListSet(lsthree)


# Hey, how about a function that creates these sets based on parameters
def divSetGen(n, divRange):
    """Return a list of 'n' sets that each contains numbers
     from 0 to 'divRange', divisible by the list index + 2 """
    return [{i for i in range(divRange+1) if i % (x+2) == 0} for x in range(n)]

lsfive = divSetGen(5, 20)
print u"\n\n My add-on: Function returns list with sets s2, s3, s4, and s5:"
displayListSet(lsfive)
