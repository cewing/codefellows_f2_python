"""Dictionary/Set lab assignment with comprehensions"""


food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

print """
      {name} is from {city}, and he likes {cake} cake, 
      {fruit} fruit, {salad} salad, and {pasta} pasta.
      """.format(**food_prefs)

hex_int_dict = {i: hex(i) for i in range(16)}
print 'hex_int_dict:', hex_int_dict

a_food_prefs = {keys: name.count('a') for keys, name in food_prefs.iteritems()} 
print 'a_food_prefs dict:', a_food_prefs

s2 = {i for i in range(21) if not i % 2}
s3 = {i for i in range(21) if not i % 3}
s4 = {i for i in range(21) if not i % 4}

print s2, s3, s4

# I think the instructions are asking for a generalized form,
# though not 100% sure...
def div_set(n):
    return {i for i in range(21) if not i % n}

print div_set(2), div_set(3), div_set(4)
