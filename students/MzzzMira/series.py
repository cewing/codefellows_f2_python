#!/usr/bin/python

def sum_series (k, m=0, n=1) :
    """ This function requires 1 must and 2 optinol parameters 
     Input :
        k : the position for the value
        m, n  : no values will run fibonacci function
                (2,1) combination will run lucas function
                other values will run other series
    """
    if k<0 : return None
    if m == 2 and n == 1 : return lucas(k)
    if m == 0 and n == 1 : return fibonacci(k)
    return sum_series (k-1, n, m+n)
    

def fibonacci(k):
    """ this function calculates the number positioned at
        nth index of fibonacci series 
        Input  : n - the position, bigger than 0
        Output : the value at nth position
    """
    if k < 0  : return None
    if k == 0 : return 0
    if k == 1 : return 1
    return fibonacci(k-1) + fibonacci (k-2)

def lucas(k) :
    """ this function calculates the number positioned at
        nth index of Lucas series 
        Input  : n - the position, bigger than 0
        Output : the value at nth position
    """
    if k < 0  : return None
    if k == 0 : return 2
    if k == 1 : return 1
    return lucas(k-1) + lucas(k-2)


if __name__ == '__main__' :
    u"""Test cases for sum_series function"""

    # fibonacci funtion test cases 
    # Input and Expected value
    fib_tests = (
        ( 0, 0),
        ( 1, 1),
        ( 2, 1),
        ( 3, 2),
        ( 4, 3),
        ( 5, 5),
        ( 6, 8),
        ( 7, 13),
    )

    for i, expected in fib_tests :
        assert fibonacci(i) == expected
    else :
        print u"Fibbonacci Tests Passed\n"


    # lucas function test cases
    # Input and Expected value
    lucas_tests = (
        ( 0, 2),
        ( 1, 1),
        ( 2, 3),
        ( 3, 4),
        ( 4, 7),
        ( 5, 11),
        ( 6, 18),
        ( 7, 29),
    )

    for i, expected in lucas_tests:
        assert lucas(i) == expected
    else :
        print u"Lucas Tests Passed\n"

        
    # sum_series_tests
    sum_series_tests = (
        (-1, 0, 1, None),
        (-1, 2, 1, None),
        ( 0, 0, 1, 0),
        ( 1, 0, 1, 1),
        ( 2, 0, 1, 1),
        ( 3, 0, 1, 2),
        ( 4, 0, 1, 3),
        ( 0, 2, 1, 2),
        ( 2, 2, 1, 3),
        ( 6, 2, 1, 18),
        ( 7, 2, 1, 29),
    )

    for i,j,k, expected in sum_series_tests :
        assert sum_series (i,j,k) == expected
    else :
        print u"Sum_series Function Tests Passed\n"

    print u"All tests pass"


