#!/usr/bin/env python

fruit = [u"Apples",u"Pears",u"Oranges",u"Peaches"]

def series1():
    print fruit
    another_fruit = raw_input(u"Please enter a fruit: ")
    fruit.append(unicode(another_fruit))
    print fruit
    aNumber = raw_input(u"Please enter a number: ")
    print aNumber + " " + fruit[int(aNumber)-1]
    fruit = [u"Starfruits"] + fruit
    print fruit
    fruit.insert(0,u"Mangos")
    print fruit

def series2():
    print fruit
    fruit.pop(-1)
    print fruit
    theLength = len(fruit)
    while len(fruit) == theLength:
        fruitDestory = raw_input(u"Please enter a fruit on the list to remove: ")
        if fruitDestory in fruit:
            fruit.remove(fruitDestory)
        else:
            print u"That fruit isn't on the list! Try again."
    print fruit

def series3():
    print fruit
    dupFruit = fruit[:]
    for aFruit in dupFruit:
        noAnswer = 1
        while noAnswer == 1:
            opinion = raw_input(u"Do you like %s yes/no:"%aFruit)
            if opinion.lower() == u"no":
                fruit.remove(aFruit)
                noAnswer = 0
            elif opinion.lower() == u"yes":
                noAnswer = 0
    print fruit

def series4():
    dupfruit = []
    for i in range(len(fruit)):
        aFruit = list(fruit[i])
        aFruit.reverse()
        aFruit = ''.join(aFruit)
        dupfruit.append(aFruit)
    print dupfruit
    fruit.pop()
    print fruit


series1()
series2()
series3()
series4()
