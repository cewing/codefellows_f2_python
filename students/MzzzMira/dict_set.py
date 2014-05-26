#!/usr/bin/python


# Homework S4 

# 1
d = {}
d['name'] = u"Chris"
d['city'] = u"Seattle"
d['cake'] = u"Chocolate"
print d
d.pop('cake')
print d
d['fruit']=u"Mango"
print d
print u"Display the dictionary keys : ", d.keys()
print u"Display the dictionary values : " , d.values()
print u"Cake is in the dictionary? ",
print 'cake' in d
print u"Mango is in the dictionary?",
print u"Mango" in d.values()

# 2) Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).
keys = []
values = []
for i in range(15) :
    keys.append(i)
    values.append(hex(i))
d1 = dict(zip(keys, values))

# 3) Using the dictionary from item 1: Make a dictionary using the same keys but with the number of a s in each value.
keys = d.keys()
values = []
for i in keys :
    values.append(d[i].lower().count('a'))
d2 = dict(zip(keys,values))

# 4) Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
    # Display the sets.
    # Display if s3 is a subset of s2 (False)
    # and if s4 is a subset of s2 (True).
s2 = set([i for i in range(20) if not i%2])
s3 = set([i for i in range(20) if not i%3])
s4 = set([i for i in range(20) if not i%4])
#print u"s2 : {} \ns2 : {}\ns4 : {}".format (s2, s3, s4)
print "\n\n\n\n"


# 5) Create a set with the letters in Python and add i to the set.
   # Create a frozenset with the letters in marathon
   # display the union and intersection of the two sets.
s_ = set('python')
s_.update('i')
fs = frozenset('marathon')
print s_.union(fs)
print s_.intersection(fs)




