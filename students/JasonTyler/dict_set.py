"""Dictionary/Set lab assignment"""

chris = {
    'name': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate'
}

print chris
del chris['cake']
print chris

chris['fruit'] = 'mango'
print "keys:", chris.keys()
print "vals:", chris.values()
print "cake is key in dict 'chris'?", bool(chris.get('cake'))
print "Mango is val in dict 'chris'?", bool(chris.values().count('Mango'))

# instructions are slightly unclear, this is my best guess for the zipped
# hex and int dict
int_dict = dict((str(int_), None) for int_ in range(16))
hex_dict = dict((hex(int_), None) for int_ in range(16))
int_hex_combo_dict = dict()

for int_, hex_ in zip(int_dict, hex_dict):
    int_hex_combo_dict.update({int_: None, hex_: None})
print int_hex_combo_dict.keys()

chris_a = dict((key, value.count('a')) for key, value in chris.items())
print "chris_a dict:", chris_a

s2 = [n for n in range(21) if n % 2 == 0]
s3 = [n for n in range(21) if n % 3 == 0]
s4 = [n for n in range(21) if n % 4 == 0]

print "set s2:", s2
print "set s3:", s3
print "set s4:", s4

print "s3 subset of s2?", s3.issubset(s2)
print "s4 subset of s2?", s4.issubset(s2)

py_str = 'Python'
py_set = set(py_str)
py_set.append
