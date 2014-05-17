#dictionaries
dictionary = {"name":"Chris","city":"Seattle","cake":"Chocolate"}
print dictionary
dictionary.pop("cake")
print dictionary
dictionary["fruit"]="Mango"
print dictionary.keys()
print dictionary.values()
print "cake" in dictionary
print "Mango" in dictionary
x=range(16)
y=(u"0",u"1",u"2",u"3",u"4",u"5",u"6",u"7",u"8",u"9",u"a",u"b",u"c",u"d",u"e",u"f")
hexDict = dict(zip(x,y))
for keys in hexDict:
    hexDict[keys]=u"a"*keys


#Sets
s = set(range(20))
s2=set([])
s3=set([])
s4=set([])

for element in s:
    if not element%2:
        s2.add(element)

for element in s:
    if not element%3:
        s3.add(element)

for element in s:
    if not element%4:
        s4.add(element)

python = set([u"p",u"y",u"t",u"h",u"o",u"n"])
python.add(u"i")

marathon =frozenset((u"m",u"a",u"r",u"a",u"t",u"h",u"o",u"n"))

print set.union(python,marathon)
print set.intersection(python,marathon)