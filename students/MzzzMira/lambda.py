#!/usr/bin/python

# Write a function that returns a list of n functions, such that each one, when called, will return the input value, incremented by an increasing number.

# Use a for loop, lambda, and a keyword argument

def func_builder(num) :
    s = []
    for i in range(num) :
        s.append(lambda x,y=i: x+y)
    return s

s_list = func_builder(5)
for f in s_list :
    print f(5)

# Extra credit : Do it with a list comprehension, instead of a for loop
def func_builder1 (num):
    s1 = [lambda x,y=i : x+y for i in range(num)]
    return s1
s1_list = func_builder1(20)


for f in s1_list :
    print f(5),
