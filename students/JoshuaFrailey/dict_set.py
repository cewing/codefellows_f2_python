import copy
# # Dictionaries
# d = {u"name": u"Chris", u"city": u"Seattle", u"cake": u"Chocolate"}
# print d
# d.pop(u"cake")
# print d
# d[u"fruit"] = u"Mango"
# print d
# print d.keys()
# print d.values()
# print (u"cake" in d)
# print (u"Mango" in d.values())
# int_to_hex = dict(zip(range(16), [hex(x) for x in range(16)]))
# print int_to_hex
# num_a = {}
# for k, v in d.items():
#     num_a[k] = d[k].count(u"a")
# print num_a

# # Sets
# s2 = set()
# s3 = set()
# s4 = set()
# for i in range(21):
#     if i % 2 == 0:
#         s2.add(i)
#     if i % 3 == 0:
#         s3.add(i)
#     if i % 4 == 0:
#         s4.add(i)
# print u"s2: {}".format(s2)
# print u"s3: {}".format(s3)
# print u"s4: {}".format(s4)
# print s3.issubset(s2)
# print s4.issubset(s2)

# python_set = set()
# for letter in u"Python":
#     python_set.add(letter)
# python_set.add(u"i")
# marathon_set = set()
# for letter in u"marathon":
#     marathon_set.add(letter)
# marathon_frozen = frozenset(marathon_set)
# print python_set.union(marathon_frozen)
# print python_set.intersection(marathon_frozen)

food_prefs = {
    u"name": u"Chris", u"city": u"Seattle", u"cake": u"chocolate",
    u"fruit": u"mango", u"salad": u"greek", u"pasta": u"lasgna"
    }
phrase = []
phrase.append(u"{name} is from {city}, and he likes {cake} cake, {fruit} ")
phrase.append(u"fruit, {salad} salad, and {pasta} pasta.")
print "".join(phrase).format(**food_prefs)
int_to_hex = dict(zip(range(16), [hex(x) for x in range(16)]))
print u"int_to_hex: {}".format(int_to_hex)
int_to_hex2 = {k: hex(k) for k in range(16)}
print u"int_to_hex2: {}".format(int_to_hex2)
num_a = food_prefs.copy()
for k, v in num_a.items():
    num_a[k] = v.count(u"a")
print u"Number of a's: {}".format(num_a)
s2 = {x for x in range(21) if x % 2 == 0}
s3 = {x for x in range(21) if x % 3 == 0}
s4 = {x for x in range(21) if x % 4 == 0}
set_list = [set(), set(), set()]
for x in range(21):
    if x % 2 == 0:
        set_list[0].add(x)
    if x % 3 == 0:
        set_list[1].add(x)
    if x % 4 == 0:
        set_list[2].add(x)
extra_credit = [{x for x in range(21) if x % s == 0} for s in range(2, 5)]
line = u"s2: {}\ns3: {}\ns4: {}\nsets: {}\nextra_credit: {}"
print line.format(s2, s3, s4, set_list, extra_credit)
