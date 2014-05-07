def fibonaccci(n):
    """Take an int 'n', return the 'nth' value in the fibonaccci series"""
    firstInt = 0
    secondInt = 1
    if n < 0:
        return None
    elif int(n) != float(n):
        return None
    elif n == 0:
        return firstInt
    else:
        for i in range(1,n):
            thirdInt = firstInt+secondInt
            firstInt = secondInt
            secondInt = thirdInt
            thirdInt = 0
        return secondInt


def lucas(n):
    """Take an int 'n', return the 'nth' value in the lucas series"""
    firstInt = 2
    secondInt = 1
    if n < 0:
        return None
    elif int(n) != float(n):
        return None
    elif n == 0:
        return firstInt
    else:
        for i in range(1,n):
            thirdInt = firstInt+secondInt
            firstInt = secondInt
            secondInt = thirdInt
            thirdInt = 0
        return secondInt


def sum_series(n,indexZero = 0,indexOne = 1):
    """Take an int 'n', and the first two values in a series, then return the 'nth' value in the sum series"""
    if n < 0:
        return None
    elif int(n) != float(n):
        return None
    elif n == 0:
        return indexZero
    else:
        for i in range(1,n):
            thirdInt = indexZero+indexOne
            indexZero = indexOne
            indexOne = thirdInt
            thirdInt = 0
        return indexOne


if __name__=='__main__':
    #Test the fibonacci function
    assert fibonaccci(0)==0
    assert fibonaccci(1.1)==None
    assert fibonaccci(2)==1
    assert fibonaccci(3)==2
    assert fibonaccci(4)==3
    assert fibonaccci(5)==5
    assert fibonaccci(6)==8
    #test the lucas function
    assert lucas(0)==2
    assert lucas(1.1)==None
    assert lucas(2)==3
    assert lucas(3)==4
    assert lucas(4)==7
    assert lucas(5)==11
    assert lucas(6)==18

    #Test the  fibonacci sum_series function
    assert sum_series(-10)==None
    assert sum_series(0)==0
    assert sum_series(1.1)==None
    assert sum_series(2)==1
    assert sum_series(3)==2
    assert sum_series(4)==3
    assert sum_series(5)==5
    assert sum_series(6)==8
    #test the lucas sum_series function
    assert sum_series(-20,2,1)==None
    assert sum_series(0,2,1)==2
    assert sum_series(1.1,2,1)==None
    assert sum_series(2,2,1)==3
    assert sum_series(3,2,1)==4
    assert sum_series(4,2,1)==7
    assert sum_series(5,2,1)==11
    assert sum_series(6,2,1)==18
    #Succes!
    print "All Tests Passed"