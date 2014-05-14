# Create Dictionary
d = dict(name='Chris', city='Seattle', cake='Chocolate')
# Display Dictionary
print d
 # Delete entry for 'cake'
del d['cake']
# Display Dictionary
print d
# Add entry for 'fruit' with 'Mango' and Display Dictionary
d['fruit'] = 'Mango'
print 'Dictionary Keys:'
for k in d.keys():
    print k
print 'Dictionary Values:'
for v in d.values():
    print v

if 'cake' in d.keys():
    print "'cake' is a key in the dictionary"
else:
    print "'cake' is not a key in the dictionary"

if 'Mango' in d.values():
    print "'Mango' is a value in the dictionary"
else:
    print "'Mango' is not a value in the dictionary"
