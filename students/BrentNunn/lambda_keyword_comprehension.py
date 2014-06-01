#!/usr/bin/env python
"""Code Fellows List Lambda and Keyword Magic assignment"""

def function_builder(list_size = 5):
    """Return a list of n functions, each of which, when called, will return
    the input value incremented by an increasing number.
    """

    return [lambda i, m=n: m + i for n in range(list_size)]


if __name__ == '__main__':
    print u"\nTesting lambda_keyword_comprehension.py."

    print u"Initializing my_funcs list with function_builder(10)"
    my_funcs = function_builder(10)

    for n in range(len(my_funcs)):
        result = my_funcs[n](0)
        assert result == n

        result = my_funcs[n](-1)
        assert result == -1 + n

        result = my_funcs[n](100)
        assert result == 100 + n

        result = my_funcs[n](100, 99)
        assert result == 100 + 99

    print u"Testing complete"
