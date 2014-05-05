"""Ackermann Function"""


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        while m > 0:
            acker = ackermann(m-1, 0)
            print acker, n
        return acker
    else:
        pass


def ackermann_tail_recursive(m,n):
    """The verbatim Ackermann function written in an if/else construction
    http://en.wikipedia.org/wiki/Ackermann_function
    Unfortunately tail recursion is a problem, and as written, this funcition
    can't be evaluated past m = 3, n = 3 """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

if __name__ == "__main__":
    import nose
    nose.run(argv=[__file__, '--with-doctest', '-vv'])
    
    nose.assert_equal(ackermann(0,0), 1)
    nose.assert_equal(ackermann(0,1), 2)
    nose.assert_equal(ackermann(0,2), 3)
    nose.assert_equal(ackermann(0,3), 4)
    nose.assert_equal(ackermann(0,4), 5)
    nose.assert_equal(ackermann(1,0), 2)
    nose.assert_equal(ackermann(1,1), 3)
    nose.assert_equal(ackermann(1,2), 4)
    nose.assert_equal(ackermann(1,3), 5)
    nose.assert_equal(ackermann(1,4), 6)
    nose.assert_equal(ackermann(2,1), 3)
    nose.assert_equal(ackermann(2,2), 7)
    nose.assert_equal(ackermann(2,3), 9)
    nose.assert_equal(ackermann(2,4), 11)
    nose.assert_equal(ackermann(3,0), 5)
    nose.assert_equal(ackermann(3,1), 13)
    nose.assert_equal(ackermann(3,2), 29)
    nose.assert_equal(ackermann(3,3), 61)
    nose.assert_equal(ackermann(3,4), 125)
    nose.assert_equal(ackermann(4,0), 13)
    nose.assert_equal(ackermann(4,1), 65533) 
