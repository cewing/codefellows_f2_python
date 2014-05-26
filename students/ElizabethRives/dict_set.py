# -*- coding: utf-8 -*-


my_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'} 
print my_dict
my_dict.pop('cake')
print my_dict
my_dict['fruit'] = 'Mango'
print my_dict
print my_dict.keys()
print my_dict.values()
print u'cake' in my_dict
print u'Mango' in my_dict.values()


y = range(16)
h_list = []
for x in y:
	h_list.append(hex(x))
new_dict = dict(zip(y, h_list))
print new_dict

new_dict = {y: hex(y) for y in range(16)}

dict_four = {}

for key in my_dict.iterkeys():
	values = my_dict[key]
	count = values.count('a')
	dict_four[key] = (count)

print dict_four


s2 = set([])
s3 = set([])
s4 = set([])

for x in range(21):
	if x%2 == 0:
		s2.update([x])
	if x%3 == 0:
		s3.update([x])
	if x%4 == 0:
		s4.update([x])

print s2, s3, s4

if s3.issubset(s2):
	print s3

if s4.issubset(s2):
	print s4


python = set(n for n in 'Python')
python.update('i')
marathon = frozenset(n for n in 'marathon')

python | marathon, python & marathon
