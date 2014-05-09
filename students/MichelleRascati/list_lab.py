#!/usr/env/python
def list():
    """Create list of "Apples", "Pears", "Oranges", "Peaches"."""
    return [u"Apples", u"Pears", u"Oranges", u"Peaches"]


def d_list(x):
    """Display a list (x)."""
    print x


def p_list(x, where):
    """Prompt user to add item to list (x) and where."""
    return raw_input(u"Add another fruit to %s of the list: " % where)


def add_end(val, x):
    """Add value (val) to the end of a list (x)"""
    return x.append(val)


def n_list(x):
    """Ask user for value of list to return (x)."""
    n = raw_input(u"What number fruit would you like?: ")
    return u"Item %i: %s" % (n, x[n - 1])


def add_plus(val, x):
    """Add value (val) to beginning of list (x) using the + operator."""
    return val + x


def add_insert(val, x):
    """Add value (val) to beginning of list (x) using the append() fucntion."""
    return x.insert(0, val)


def begin_with(char, x):
    """Display values from list (x) that begin with char."""
    for val in x:
        if val[0] == char:
            print val

if __name__ == '__main__':
    # Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    fruits = list()
    # Display the list.
    d_list(fruits)
    # Ask the user for another fruit and add it to the end of the list.
    add_end(p_list(fruits, u'end'), fruits)
    # Display the list.
    d_list(fruits)
    # Ask the user for a number and display the number back to
    # the user and the fruit corresponding to that number.
    n_list(fruits)
    # Add another fruit to the beginning of the list using “+” and display.
    add_plus(p_list(fruits, u'beginning'), fruits)
    # Add another fruit to the beginning of the list using insert() & display.
    add_insert(p_list(fruits, u'beginning'), fruits)
    # Display all the fruits that begin with “P”, using a for loop.
    begin_with("P", fruits)
