def ack(m, n):
    """Return value of Ackermann function"""
    if m < 0 or n < 0 or not isinstance(m, int) or not isinstance(n, int):
        return None


if __name__ == '__main__':
    print 'module has been run, testing function:'

    vals = [[0,0,1], [0,1,2], [0,2,3], [0,3,4], [0,4,5],
    [1,0,2], [1,1,3], [1,2,4], [1,3,5], [1,4,6],
    [2,0,3], [2,1,5], [2,2,7], [2,3,9], [2,4,11],
    [3,0,15], [3,1,13], [3,2,29], [3,3,61], [3,4,125],
    [4,0,13], [4,1,65533], [4,(2**265536) - 3], [4,3,(2**(2**265536)) - 3], [4,4,(2**(2**265536(2**265536))) - 3]
    ]

    test = True #initialize test

    for val in vals:
        # test will return False if any ack(m,n) results are not correct
        test = test and ack(val[0], val[1]) == val[3] #True or False?

    if test == True:
        print "All Tests Pass"
