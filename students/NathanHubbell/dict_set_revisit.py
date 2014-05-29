#dictionaries
dictionary = {u"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}
print u"My name is {name} and I live in {city} where I eat {fruit} for breakfast, {salad} for lunch, {pasta} for dinner, and {cake} for dessert.".format(**dictionary)

y=(u"0",u"1",u"2",u"3",u"4",u"5",u"6",u"7",u"8",u"9",u"a",u"b",u"c",u"d",u"e",u"f")

new_dict = {i:y[i] for i in range(16)}
print new_dict

new_foodDict = {key:dictionary[key].count(u"a") for key in dictionary}

s1 = range(21)
s2=set()
s3=set()
s4=set()
s5=set()

sLists_empty=[s2,s3,s4,s5]
sLists_full=[]

for count,element in enumerate(sLists_empty):
    element = {i for i in s1 if not i%(count+2)}
    sLists_full.append(element)


print sLists_full