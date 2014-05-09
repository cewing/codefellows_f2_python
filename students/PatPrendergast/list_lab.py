#!/usr/bin/env python

#list_lab.py


def printer(t):
    ''' prints a list vertical line by line'''
    for e in t:
        print e

def section():
    print ""
    print "---.---.---"
    print ""

def preference(t):
    ''' a yes or no for a user to answer for a preference'''   
    for e in t[:]:
        e.lower
        asked = raw_input(u'Do you like %s? y or n> ' % e)
        while asked not in ['y', 'n']:
            asked = raw_input(u"Please answer 'y' or 'n' >")   
        if asked.lower() == 'n':
            t.remove(e)
        else:
            continue


section()
fruit = [u'Apples', u'Pears', u'Oranges', u'Peaches']

print u'Here is a list of fruit:'
printer(fruit)
section()

add_fruit = raw_input(u'What fruit would you like to add? ')
fruit.append(add_fruit)

print ''
print u'New Fruit List:' 
printer(fruit)
section()

get_num = int(raw_input(u'The fruit is numbered.  Enter a number up to %s: ' % len(fruit)))
print 'Fruit #%i is %s' % (get_num, fruit[get_num-1])

# While not necessary, new_fruit, will help with index practice.
new_fruit = [u'Strawberries']
print '---.---'
print u"Adding fruit to the front of the list..."
print u"Starting with %s" % new_fruit
print ''
print u'The list now:'
printer(new_fruit + fruit)


new_fruit.append('Bananas')
print '---.---'
print "Adding fruit to the front of the list.  This time %s." % new_fruit[1]
fruit.insert(0, new_fruit[1])

print ''
print u'The list now:'
printer(fruit)
print ''
print 'Who ate the %s?' % new_fruit[0]
section()

print u"Now the fruit that starts with 'P'."
for e in fruit:
    if e[0] == 'P':
        print e

print ""
print ""
print u"Here is the list at this point:"
printer(fruit)
print ''
print u"We'll eat the last one there."

fruit.pop()
print ""
print u"Yum."
print ""
printer(fruit)

take_away =  raw_input(u'Which fruit would you like to take with you? ')
for e in fruit:
    if take_away == e:
        fruit.remove(e)

print ""
print u"They're yours."
print ""
printer(fruit)
section()

print u"I am going ask about your preferences."
preference(fruit)
print ''
print u'What you like best: '
printer(fruit)
section()

fruit2 = fruit[:]

for e in fruit2:
    print e[::-1]

if fruit != []:
    fruit.pop()

section()
printer(fruit)
print ''


#start()
#adding()



    