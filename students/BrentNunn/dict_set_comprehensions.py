#!/usr/bin/env python

dict_lab = {u"name": u"Chris", u"city": u"Seattle", u"cake": u"Chocolate",
            u"fruit": u"mango", u"salad": u"greek", u"pasta": u"lasagna"}
print (u"{name} is from {city}, and he likes {cake} cake, {fruit} fruit, "
       u"{salad} salad, and {pasta} pasta.\n".format(**dict_lab))

dict_a_count = {item[0]: item[1].count('a') for item in dict_lab.iteritems()}
print u"dict_lab count of 'a's:"
for item in dict_a_count:
    print u"\t{} has {} 'a'".format(dict_lab[item], dict_a_count[item])

print u"\nDecimal to hex dictionaries:"
dec_to_hex_dict = dict([(num, hex(num)) for num in range(16)])
print dec_to_hex_dict, '\n'

dec_to_hex_dict = {num: hex(num) for num in range(16)}
print dec_to_hex_dict, '\n'

s2 = {n for n in range(21) if n % 2 == 0}
print u"s2 = {}\n".format(s2)

s3 = {n for n in range(21) if n % 3 == 0}
print u"s3 = {}\n".format(s3)

s4 = {n for n in range(21) if n % 4 == 0}
print u"s4 = {}\n".format(s4)

s_list = []
for m in (2, 3, 4):
    s_list.append({n for n in range(21) if n % m == 0})

print u"s_list = {}\n".format(s_list)

s_list2 = [{n for n in range(21) if n % m == 0} for m in (2, 3, 4)]

print u"s_list2 = {}\n".format(s_list2)

print u"Too much fun."


