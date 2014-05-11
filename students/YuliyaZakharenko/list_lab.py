fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print 'There are following fruits in the basket: ', fruits
new_fruit = raw_input('What fruit would you like to add')
fruits.append(new_fruit)
print 'Now there are following fruits in the basket: ', fruits
i = raw_input('Enter a number from 1 to 5')
i = int(i)
print i, fruits[i-1]
fruits = ['Papayas'] + fruits
print fruits
fruits.insert(0, 'Apricots')
print fruits
Pfruits = []
for i in range(0, len(fruits)):
    if fruits.startswith('P'):
        Pfruits.append(fruits[i])
print Pfruits   
print fruits
fruits.pop() 
print fruits
fruit_del = raw_input('What fruit to delete')
if fruit_del in fruits:
    fruits.remove(fruit_del)
else:
    print fruit_del, "cannot be deleted because it is not in the fruits"
print fruits
fruits *= 2
print fruits
while fruit_del not in fruits:
    fruit_del = raw_input('What fruit to delete')
    if fruit_del in fruits:
        for fruit_del in fruits:
            fruits.remove(fruit_del)
    else:
        print fruit_del, "cannot be deleted because it is not in the fruits"
print fruits
fruit = fruits[0].lower()
fruit_like = raw_input("Do you like %s" %fruit)
print fruit_like





