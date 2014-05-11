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

series1()