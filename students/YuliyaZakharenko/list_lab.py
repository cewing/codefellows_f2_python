#! /usr/bin python
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
    if fruits[i].startswith('P'):
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
fruit_del2 = raw_input('What fruit to delete')
if fruit_del2 in fruits:
    #for loop didn't work, while loop work
    while fruit_del2 in fruits:
        fruits.remove(fruit_del2)
else:
    while fruit_del2 not in fruits:
        print fruit_del, "cannot be deleted because it is not in the fruits"
print fruits
print len(fruits)
# for i in range(len(fruits[:])) didn't work
# need to figure out how to ask only once about a fruit even if there are multiple occurences in the copy of the list. 
# then use while loop to delete all the occurences
for i in fruits[:]:
    fruit = i.lower()
    fruit_like = raw_input("Do you like %s" %fruit)
    if fruit_like in ['No', 'no']:
        fruits.remove(i)
    elif fruit_like in ['Yes', 'yes']:
        pass
    else:
        while fruit_like not in ['No', 'no', 'Yes', 'yes']:
            fruit_like = raw_input("Please enter Yes or No")
print fruits





