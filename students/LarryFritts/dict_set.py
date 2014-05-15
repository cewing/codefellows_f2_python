#!/usr/local/bin/python

print u"\n\nSeries 1...............................\n\n"

def hasValue(str):
    """Checks to see if the dict has a value"""
    for x in dict_first.values():
        if x == str:
            return True

    return False

dict_first = {u"name": u"Chris", u"city": u"Seattle", u"cake": u"Chocolate"}
print dict_first, "\n"
dict_first.pop(u"cake")
print dict_first, "\n"
dict_first.setdefault(u"fruit", u"Mango")
print dict_first, "\n"
print dict_first.viewkeys(), "\n"
print dict_first.viewvalues(), "\n"
print u"Is 'cake' in dictionary? %s" % (u"cake" in dict_first), "\n"
print u"Is 'Mango' in dictionary? %s" % hasValue(u"Mango"), "\n"

print u"\n\nSeries 2...............................\n\n"

a = tuple(range(16))
b = []
for x in range(16):
    b.append(hex(x))
b = tuple(b)
dict_second = dict(zip(a, b))
print dict_second, "\n"

print u"\n\nSeries 3...............................\n\n"
dict_third = dict_first.copy()
for k, v in dict_third.items():
    count = 0
    for c in v:
        if c == u'a':
            count += 1
    dict_third[k] = count
print dict_first
print dict_third, "\n"

print u"\n\nSeries 4...............................\n\n"
s2 = set()
for x in range(21):
    if x % 2 == 0:
        s2.add(x)
print u"s2 : %s" % s2, "\n"

s3 = set()
for x in range(21):
    if x % 3 == 0:
        s3.add(x)
print u"s3 : %s" % s3, "\n"

s4 = set()
for x in range(21):
    if x % 4 == 0:
        s4.add(x)
print u"s4 : %s" % s4, "\n"

print u"Is s3 a subset of s2? %s" % s3.issubset(s2), "\n"
print u"Is s4 a subset of s2? %s" % s4.issubset(s2), "\n"

print u"\n\nSeries 5...............................\n\n"
sPython = set(['P', 'y', 't', 'h', 'o', 'n'])
sPython.add('i')
sMarathon = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
print u"The intersection of 'Python' and 'marathon' is %s" % sPython.intersection(sMarathon), "\n"
print u"The union of 'Python' and 'marathon' is %s" % sPython.union(sMarathon), "\n"