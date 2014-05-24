# -*- coding: utf-8 -*-


food_prefs = {u"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}


print u'{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.'.format(**food_prefs)

num_hex = dict((i, hex(i)) for i in range(16))

num_hex = {i: hex(i) for i in range(16)}

x = list(food_prefs.keys())
y = list(i.count('a') for i in food_prefs.values())
new_food_prefs = {k: v for (k, v) in zip(x, y)}

s2 = set(i for i in range(21) if i%2 == 0)
s3 = set(i for i in range(21) if i%3 == 0)
s4 = set(i for i in range(21) if i%4 == 0)

divisible = set(range(21))
s2_new = set()
s3_new = set()
s4_new = set()

for i in divisible:
	if i%2 == 0:
		s2_new.add(i)
	if i%3 == 0:
		s3_new.add(i)
	if i%4 == 0:
		s4_new.add(i)
