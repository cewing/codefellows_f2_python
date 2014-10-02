#!/usr/bin/env python

"""
Example code for using lambda, keywords, and keyword scope


The challenge:

Write a function that returns a list of n functions,
such that each one, when called, will return the input value,
incremented by an increasing number.

You should use a for loop, lambda, and a keyword argument

extra credit: do it with a list comprehension, instead of a for loop

"""


def function_builder(n):

    l = []
    for i in range(n):
        l.append( lambda x, i=i: x+i )
    return l


def function_builder2(n):

    return [ lambda x, i=i: x+i for i in range(n) ]


if __name__ == "__main__":
    ## some simples tests

    # uncomment to test second version
    # function_builder = function_builder2

    """
    the function should return a list of the length input
    """
    assert len(function_builder(0)) == 0

    assert len(function_builder(3)) == 3

    assert len(function_builder(5)) == 5

    """
    the functions in the list should increment the input values
    """
    func_list = function_builder(5)

    assert func_list[0](3) == 3

    assert func_list[1](3) == 4

    assert func_list[2](3) == 5

    assert func_list[3](3) == 6


    func_list = function_builder(10)

    assert func_list[0](12) == 12

    assert func_list[1](10) == 11

    assert func_list[9](3) == 12

    print "you got this far without assertions failing: all good"

