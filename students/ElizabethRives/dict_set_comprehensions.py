


food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}


print u'{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.'.format(**food_prefs)

num = [] 

num = {i: hex(i) for i in range(16)}

new_food_prefs = {}

s2 = set(i for i in range(21) if i%2 == 0)
s3 = set(i for i in range(21) if i%3 == 0)
s4 = set(i for i in range(21) if i%4 == 0)

s = set(range(21))
s2_new = set()
s3_new = set()
s4_new = set()

for i in s:
	if i%2 == 0:
		s2_new.add(i)
	if i%3 == 0:
		s3_new.add(i)
	if i%4 == 0:
		s4_new.add(i)
