#!/usr/bin/env python
"""Code Fellows List Comprehensions assignment, Count Evens"""

def count_evens(nums):
    """Count the number of even ints in given array"""

    return len([num for num in nums if num % 2 == 0])

if __name__ == '__main__':
    print u"\nTesting count_evens.py."

    test = []
    result = count_evens(test)
    print u"The number of evens in list {} is {}".format(test, result)

    test = [0]
    result = count_evens(test)
    print u"The number of evens in list {} is {}".format(test, result)

    test = [2, 4, 6, 100, 1000, 100000]
    result = count_evens(test)
    print u"The number of evens in list {} is {}".format(test, result)

    test = [1, 3, 13, 19, 99]
    result = count_evens(test)
    print u"The number of evens in list {} is {}".format(test, result)

    test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = count_evens(test)
    print u"The number of evens in list {} is {}".format(test, result)

