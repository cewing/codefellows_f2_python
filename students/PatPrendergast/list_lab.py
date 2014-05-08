#!/usr/bin/env python

#list_lab.py


def printer(t):
    for e in t:
        print e

def section():
    print ""
    print "---.---.---"
    print ""

def preference(t):   
    for e in t[:]:
        e.lower
        asked = raw_input('Do you like %s? y or n> ' % e)
        if asked.lower() == 'y':
            continue
        elif asked.lower() == 'n':
            t.remove(e)
            continue
        else:  #This is not quite it...
            while asked != 'y' or asked != 'n':
                print "Please answer 'y' or 'n' >"
                print''
                preference(t)

section()
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']

print 'Here is a list of fruit:'
printer(fruit)
section()

add_fruit = raw_input('What fruit would you like to add? ')
fruit.append(add_fruit)

print ''
print 'New Fruit List:' 
printer(fruit)
section()

get_num = int(raw_input('The fruit is numbered.  Enter a number up to %s: ' % len(fruit)))
print 'Fruit #%i is %s' % (get_num, fruit[get_num-1])

# While not necessary, new_fruit, will help with index practice.
new_fruit = ['Strawberries']
print '---.---'
print "Adding fruit to the front of the list..."
print "Starting with %s" % new_fruit
print ''
print 'The list now:'
printer(new_fruit + fruit)


new_fruit.append('Bananas')
print '---.---'
print "Adding fruit to the front of the list.  This time %s." % new_fruit[1]
fruit.insert(0, new_fruit[1])

print ''
print 'The list now:'
printer(fruit)
print ''
print 'Who ate the %s?' % new_fruit[0]
section()

print "Now the fruit that starts with 'P'."
for e in fruit:
    if e[0] == 'P':
        print e

print ""
print ""
print "Here is the list at this point:"
printer(fruit)
print ''
print "We'll eat the last one there."

fruit.pop()
print ""
print "Yum."
print ""
printer(fruit)

take_away =  raw_input('Which fruit would you like to take with you? ')
for e in fruit:
    if take_away == e:
        fruit.remove(e)

print ""
print "They're yours."
print ""
printer(fruit)
section()

print "I am going ask about your preferences."
preference(fruit)
print 'What you like best: '
printer(fruit)
section()


#start()
#adding()



    