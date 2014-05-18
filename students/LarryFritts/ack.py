"""Ackerman's Function"""

def ack(m, n):

    """
    Evaluate Ackerman's Function.

    This function is recursive and can only be used for m <= 3 and
    n <= 4.
    """

    if not (isinstance(m, int) and m >= 0) or not (isinstance(n, int) and n >= 0):
        return None

    if m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

if __name__ == "__main__":
    """Assertion testing for Ackerman's Function"""

    #from Wiki on Ackermann's Function
    testTable = [1, 2, 3, 4, 5,
                 2, 3, 4, 5, 6,
                 3, 5, 7, 9, 11,
                 5, 13, 29, 61, 125]

    count = 0
    for m in range(4):
        for n in range(5):
            assert(ack(m, n) == testTable[count])
            count += 1

    print "Passed all tests"
