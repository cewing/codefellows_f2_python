# functions with intentional errors


def name_error(bar):
    # foo not defined before call
    foo += 1
    foobar = foo + bar
    return foobar


def type_error(string, number):
    # python is strongly typed, won't concatenate string to int
    return string + number


def syntax_error();
    # I've done the semi-colon thing too many times...
    return "Don't you hate that semi-colon is part of the same key?"


def attribute_error(list, number_to_add):
    # list doesn't have an "add" function
    return list.add(number_to_add)
