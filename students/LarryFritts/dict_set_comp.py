#!/usr/local/bin/python


dict_first = {u"name": u"Chris", u"city": u"Seattle", u"cake": u"Chocolate",
              u"fruit": u"mango", u"salad": u"greek", u"pasta": u"lasagna"}

print """\n\n{name} is from {city}.  His food preferences are {cake} cake,
         {fruit} fruit, {salad} salad, and {pasta} pasta.""".format(**dict_first)


dict_num = dict(zip((i for i in range(16)), (hex(k) for k in range(16))))
print "\n\nlist comprehension numbers: hex-numbers: ", dict_num

dict_num = {num: hex(num) for num in range(16)}
print "\n\ndict comprehension numbers: hex-numbers: ", dict_num

dict_count = {key: value.count('a') for key, value in dict_first.iteritems()}
print "\n\nAnd for the count of a's :", dict_count

s2 = {i for i in range(21) if not i%2}
s3 = {i for i in range(21) if not i%3}
s4 = {i for i in range(21) if not i%4}
print "\n\nSets from single line specific comprehension: ", s2, s3, s4

def create_set(i):
    return {k for k in range(21) if not k%i}
print "\n\nSets from generic comprehension: ", create_set(2), create_set(3), create_set(4)