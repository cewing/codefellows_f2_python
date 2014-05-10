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
            firstInt,secondInt = secondInt,(firstInt+secondInt)
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
            firstInt,secondInt = secondInt,(firstInt+secondInt)
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
            indexZero,indexOne = indexOne,(indexZero+indexOne)
        return indexOne


if __name__=='__main__':
    fibList = [None,0,1,1,2,3,5,8]
    lucList = [None,2,1,3,4,7,11,18]
    #Test the fibonacci function
    for i in range(8):
        assert fibonaccci(i-1)==fibList[i]

    #test the lucas function
    for i in range(8):
        assert lucas(i-1)==lucList[i]

    #Test the  fibonacci sum_series function
    for i in range(8):
        assert sum_series(i-1)==fibList[i]

    #test the lucas sum_series function
    for i in range(8):
        assert sum_series(i-1,2,1)==lucList[i]

    #Succes!
    print "All Tests Passed"