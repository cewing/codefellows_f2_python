#!/usr/bin/python

def print_ (fruits) :
    print u"Fruits in the list are : " ,
    for i in range(len(fruits)) :
        print fruits[i],
    print
    print

def ask_new_fruit (fruits, is_for_add=True) :
    q = u""
    if is_for_add : 
        q = u"Enter a fruit to add : "
    else :
        q = u"Enter a fruit to delete : "
    while True :
        new_fruit = raw_input(q)
        new_fruit = unicode(new_fruit)
        already_in_list = new_fruit in fruits
        if (already_in_list==True and is_for_add==False) or (already_in_list==False and is_for_add==True) :
            break
        elif already_in_list == True :
            print u"This fruit is already in the list! Please enter a new one!"
        else :
            print u"This fruit is not in the list! Please choose from the list!", print_(fruits)
    return new_fruit

#Create a list
fruits = [u"Apples",u"Pears",u"Oranges",u"Peaches"]

#Display the list
print_ (fruits)

#Ask user another fruit and add it to the end of the list
fruits.append(ask_new_fruit (fruits))

#display the list
print_ (fruits)

#Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
num = int (raw_input("Enter a number:"))
while num < 1 or num > len(fruits) :
    num = int (raw_input("Enter a valid number:"))
print "The fruit in %i position is %s\n" % (num, fruits[num-1])

# Add another fruit to the beginning of the list using + and display the list.
fruits = [ask_new_fruit (fruits)] + fruits
print_ (fruits)

#Add another fruit to the beginning of the list using insert() and display the list.
fruits.insert(0,ask_new_fruit (fruits))
print_ (fruits)


# Display all the fruits that begin with P, using a for loop.
print u"All the fruits that begin with P : ",
for i in range(len(fruits)) :
    if fruits[i][0].lower() != u"p" : continue
    print fruits[i],
print "\n"


#display the list
print_ (fruits)


#Remove the last fruit from the list
print u"Last fruit is removed from list!"
fruits.pop(-1)

#display the list
print_ (fruits)

#Ask the user for a fruit to delete and find it and delete it.
fruits.remove(ask_new_fruit (fruits, False))
#display the list
print_ (fruits)


#Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences
fruits = 2*fruits
while True :
    new_ = unicode(raw_input("Enter a fruit to find a match :"))
    if (new_ in fruits) :
        break
cp_fruits = fruits[:]
for i in range(len(cp_fruits)-1) :
    for j in range(i+1, len(cp_fruits)) :
        if cp_fruits[i] == cp_fruits[j] :
            fruits.remove(cp_fruits[i])
            break
print_(fruits)





#Ask the user for input displaying a line like Do you like apples?
#for each fruit in the list (making the fruit all lowercase).
copy_fruits = fruits[:]
for i in copy_fruits :
    new_ = unicode(raw_input("Do you like %s? :"%i.lower()))
    while new_ != u"yes" and new_ !=u"no" :
        print u"PLease enter yes or no! \n"
        new_ = unicode(raw_input("Do you like %s? :"%i.lower()))
    if new_ == u"no" :
        fruits.remove(i)
print_ (fruits)


cp_fruits = fruits[:]
for i in range(len(cp_fruits)) :
    cp_fruits[i] = cp_fruits[i][::-1]
print (u"Reverse order list : "),
print_ (cp_fruits)





