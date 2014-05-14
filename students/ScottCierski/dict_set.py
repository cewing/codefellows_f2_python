print u"Establishing initial dictionary 's1'..."
s1 = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}
print s1
print u""

print u"Removing 'cake' from s1..."
s1.pop('cake')
print s1
print u""

print u"Adding 'fruit' : 'Mango' to s1..."
s1.setdefault('fruit', 'Mango')
print s1
print u""

print u"Here are all the current keys in s1:"
for k in s1.keys():
    print k
print u""

print u"Here are all the current values in s1:"
for v in s1.values():
    print v
print u""

print u"Is 'cake' among the current keys in s1?"
is_cake_in_s1 = 'cake' in s1.keys()
print is_cake_in_s1
print u""

print u"Is 'Mango' among the current values in s1?"
is_mango_in_s1 = 'Mango' in s1.values()
print is_mango_in_s1
print u""

# Create a dict of integers 0 through 15 and their hex values
keys = []
values = []
for i in range(16):
    keys.append(i)
    values.append(hex(i))
z1 = dict(zip(keys, values))
print z1