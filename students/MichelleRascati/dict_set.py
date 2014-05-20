### 1 ###
# Create Dictionary
food_prefs = dict(name=u'Chris', city=u'Seattle', cake=u'Chocolate',
            fruit=u'mango', salad=u'greek', pasta=u'lasagna')
# Display Dictionary
print '1) {} is from {}, and he likes {} cake, {} fruit, {} salad, and {} pasta.'.format(
    food_prefs['name'], food_prefs['city'], food_prefs['cake'], food_prefs['fruit'],
    food_prefs['salad'], food_prefs['pasta'])


### 2 ###
# Create list of 0-15
z_15 = range(16)
# Create list of 0-15 in hexidecimal
hex_z_15 = [hex(num) for num in z_15 ]
# Zip two lists to make a dictionary
d_hex = dict(zip(z_15, hex_z_15))

print '2) 0-15 and hex values:', d_hex

### 3 ###
# Create dict of hex values with dict comprehension
hex_dict = {i: hex(i) for i in range (16)}

print '3) 0-15 and hex values:', hex_dict

### 4 ###
# Make a dictionary with keys in d number of 'a's as vals
food_prefs_a = {k:food_prefs[k].count('a') for k in food_prefs.keys()}

print "4) Number of a's in original dict", food_prefs_a

### 5 ###
# Create a set of containing 0-20 divisible by 2, 3, and 4 respectively
s2 = {n for n in range(21) if n%2}
s3 = {n for n in range(21) if n%3}
s4 = {n for n in range(21) if n%4}

print 's2:', s2
print 's3:', s3
print 's4:', s4
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
