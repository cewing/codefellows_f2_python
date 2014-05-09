def A(m,n):
    """Return a value based on the Ackermann function"""
    if m < 0 or n < 0:
        return None
    elif m == 0:
        return n+1
    elif m>0 and n ==0:
        return A(m-1, 1)
    else:
        return A(m-1, A(m,n-1))     
if __name__ == "__main__":
    #list of lists containing the inputs and expected output to iterate through.
    vals = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5],
            [1, 0, 2], [1, 1, 3], [1, 2, 4], [1, 3, 5], [1, 4, 6],
            [2, 0, 3], [2, 1, 5], [2, 2, 7], [2, 3, 9], [2, 4, 11],
            [3, 0, 5], [3, 1, 13], [3, 2, 29], [3, 3, 61], [3, 4, 125]
            ]
    #iterating through vals list and asserting that ackermann function returns value at index 2 
    # when suplied with the parameters at index 0 and 1 from val list

    for val in vals:
        assert A(val[0], val[1]) == val[2]
    
    assert A(-1, 1) == None
    print "All Tests Pass"