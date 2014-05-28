#!/usr/bin/python
import copy

# 1
food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

# Print the dict by passing it to a string format method, so that you get something like:
# Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta
print u"{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta\n".format (**food_prefs)


# Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).
d = dict([(key, hex(key)) for key in range(15)])

# Do the previous entirely with a dict comprehension should be a one liner
d1 = {key:hex(key) for key in range(15)}

# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of As in each value. You can do this either by editing the dict in place, or making a new one. If you edit in place, make a copy first!
tmp_foods = {key:value.count('a') for key, value in food_prefs.iteritems()}


# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
# Do this with one set comprehension for each set.
s2 = {i for i in range(1,20) if not i%2}
s3 = {i for i in range(1,20) if not i%3}
s4 = {i for i in range(1,20) if not i%4}    
    
# What if you had a lot more than 3
# create a sequence that holds all three sets
# loop through that sequence to build the sets up  so no repeated code.
s = []
for j in range(2,5) :
    s.append({i for i in range(1,20) if not i%j})
print s

# Extra credit: do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK, that may be getting carried away!)
s1 = [{i for i in range(1,20) if not i%j} for j in range(2,5)]
print s1


