
# Fibonacci
def fibo (n):
    ''' computes the Fibonacci series to n '''
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


# Lucas
def lucas(n):
    ''' computes the lucas series to n '''
    if n == 0:
        return 2
    elif  n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


# Fibonacci or Lucas, you chooose
def sum_series(n, o=0, p=1):
    ''' 
    Computes Fibonacci, Lucas or other series based on parameters added.

    If no optional parameters (o & p) are added, the Fibonacci function is called on n.
    Otherwise, the Lucas function is called with the optional parameters
    '''

    if n == 0:
        return o
    elif  n == 1:
        return p
    else:
        return sum_series(n-1, o, p) + sum_series(n-2, o, p)

print fibo(-1)
print fibo(0)
print fibo(1)
print fibo(2)
print fibo(3)
print fibo(4)
print fibo(5)
print u'------'
print lucas(0)
print lucas(1)
print lucas(2)
print lucas(3)
print lucas(4)
print lucas(5)
print u'------'
print u'Fibonacci: ', sum_series(2, 0, 1)
print u'Lucas: ', sum_series(5, 2, 1) 


if __name__ == "__main__":
    """Test sequences against expected normal output and rubbish input."""

    fibo_nums = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
    ]

    lucas_nums = [
        (0, 2),
        (1, 1),
        (2, 3),
        (3, 4),
        (4, 7),
        (5, 11),
        (6, 18),
        (7, 29),
        (8, 47),
        (9, 76),
    ]


for input, output in fibo_nums:
    assert fibo(input) == output


    for e in [3.5, 'a', [2,3,4]]:
        try:
            result = fibo(e)
        except ValueError:
            pass
        else:
            print u"a bad value did not raise the expected error"
            assert(False)

    print "All tests pass"
"""
for input, output in lucas_nums:
    assert lucas(input) == output

"""

