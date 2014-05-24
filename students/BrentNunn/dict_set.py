#!/usr/bin/env python

dict_lab = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print dict_lab

dict_lab.pop("cake")
print dict_lab

dict_lab["fruit"] = "Mango"
print 'dict_lab keys = ', dict_lab.keys()
print 'dict_lab values = ', dict_lab.values()
print 'Is key "cake" in dict_lab? ', "cake" in dict_lab
print 'Is value "Mango" in dict_lab? ', "Mango" in dict_lab.values()

ints = []
hexes = []
for i in range(16):
    ints.append(i)
    hexes.append(hex(i))
hex_dict = dict(zip(ints, hexes))
print 'hex_dict = ', hex_dict

dict_a_count = {}
for k, v in dict_lab.items():
    dict_a_count[k] = v.count('a')
print 'dict_a_count = ', dict_a_count

twos = set()
threes = set()
fours = set()
for n in range(21):
    if n % 2 == 0:
        twos.add(n)
    if n % 3 == 0:
        threes.add(n)
    if n % 4 == 0:
        fours.add(n)
print 'set twos = ', twos
print 'set threes = ', threes
print 'set fours = ', fours
print 'threes is a subset of twos: ', threes.issubset(twos)
print 'fours is a subset of twos: ', fours.issubset(twos)

pythonset = set('Python')
pythonset.add('i')
marathonset = frozenset('marathon')
print 'pythonsen = ', pythonset
print 'marathonset = ', marathonset
print 'pythonset union marathonset = ', pythonset.union(marathonset)
print 'pythonset intersect marathonset = ', pythonset.intersection(marathonset)


