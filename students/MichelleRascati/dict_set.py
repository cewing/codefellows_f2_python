### 1 ###
# Create Dictionary
food_prefs = dict(name=u'Chris', city=u'Seattle', cake=u'Chocolate',
            fruit=u'mango', salad=u'greek', pasta=u'lasagna')
# Display Dictionary
print '1) {} is from {}, and he likes {} cake, {} fruit, {} salad, and {} pasta.'.format(
    food_prefs['name'], food_prefs['city'], food_prefs['cake'], food_prefs['fruit'],
    food_prefs['salad'], food_prefs['pasta'])

break
### 2 ###
# Create list of 0-15
z_15 = range(16)
# Create list of 0-15 in hexidecimal
hex_z_15 = []
for num in z_15:
    hex_z_15.append(hex(num))
# Zip two lists to make a dictionary
d_hex = dict(zip(z_15, hex_z_15))

print '0-15 and hex values:', d_hex

### 3 ###
# Make a dictionary with keys in d number of 'a's as vals
d_a = {}
for k in d.keys():
    d_a[k] = d[k].count('a')

print "Number of a's in original dict", d_a

### 4 ###
# Create a set of containing 0-20 divisible by 2, 3, and 4 respectively
s2 = set()
s3 = set()
s4 = set()
for n in range(21):
    if n % 2 == 0:
        s2.add(n)
    if n % 3 == 0:
        s3.add(n)
    if n % 4 == 0:
        s4.add(n)
print s2
print s3
print s4
# Display if s3 is subset of s2
print s3.issubset(s2)
# Display if s4 is subset of s2
print s4.issubset(s2)

### 5 ###
sP = {'P', 'y', 't', 'h', 'o', 'n'}
sP.add('i')
frozen = frozenset({'m', 'a', 'r', 'a', 't', 'h', 'o', 'n'})
print "Union:", sP.union(frozen)
print "Intersection:", sP.intersection(frozen)
