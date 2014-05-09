def ack(m,n):
    """Perform the Ackermann algorithm on two inputs and return the result."""
    if m<0 or n<0:
        return None
    elif m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))

if __name__ == '__main__':

    ackFunc = [[1,2,3,4,5],[2,3,4,5,6],[3,5,7,9,11],[5,13,29,61,125]]

    for m in range(4):
        for n in range(5):
            assert ack(m,n) == ackFunc[m][n]

    print "All Tests Pass"