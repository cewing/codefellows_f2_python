def ack(m, n):
    """Return value of Ackermann function"""
    #if m < 0 or n < 0 or not isinstance(m, int) or not isinstance(n, int):
    #    return None
    if m == 0:
        f = n + 1
    elif m > 0 and n == 0:
        f = ack(m - 1, 1)
    elif m > 0 and n > 0:
        f = ack(m - 1, ack(m, n - 1))
    else:
        # This will include if m or n <0 or not number
        return None
    return f

if __name__ == '__main__':
    print 'module has been run, testing function:'

    vals = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5],
            [1, 0, 2], [1, 1, 3], [1, 2, 4], [1, 3, 5], [1, 4, 6],
            [2, 0, 3], [2, 1, 5], [2, 2, 7], [2, 3, 9], [2, 4, 11],
            [3, 0, 15], [3, 1, 13], [3, 2, 29], [3, 3, 61], [3, 4, 125]
            ]

    test = True   # Intialize Test

    for val in vals:
        # test will return False if any ack(m,n) results are not correct
        test = test and ack(val[0], val[1]) == val[3]   # True or False?

    if test:
        print "All Tests Pass"
