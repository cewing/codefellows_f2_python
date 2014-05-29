#dictionaries
food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}
print '%(name)s is from %(city)s, and he likes %(cake)s cake, %(fruit)s fruit, %(salad)s salad, and %(pasta)s pasta' % food_prefs


set= dict([(number, hex(number)) for number in (range(16))])
print set

food_prefs_new = dict([(k, v.count('a')) for k, v in food_prefs.items()])
print food_prefs_new



#sets

s2 = {i for i in range(21) if not i % 2}
s3 = {i for i in range(21) if not i % 3}
s4 = {i for i in range(21) if not i % 4}
print s2, s3, s4 

s = []
for y in (2,3,4):
    s.append({i for i in range(21) if not i % y})
print s    


s = [{i for i in range(21) for y in (2,3,4) if not i % y}]
print s

