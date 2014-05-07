def fibonaccci(n):
    """Take an int 'n', return the 'nth' value in the fibonaccci series"""
    firstInt = 0
    secondInt = 1

    if n<0:
        return None
    elif int(n)!=float(n):
        return None
    elif n==0:
        return firstInt
    else:
        for i in range(1,n):
            thirdInt = firstInt+secondInt
            firstInt=secondInt
            secondInt=thirdInt
            thirdInt=0
        return secondInt

print fibonaccci(0)

def lucas(n):
    """Take an int 'n', return the 'nth' value in the lucas series"""
    firstInt = 2
    secondInt = 1

    if n<0:
        return None
    elif int(n)!=float(n):
        return None
    elif n==0:
        return firstInt
    else:
        for i in range(1,n):
            thirdInt = firstInt+secondInt
            firstInt=secondInt
            secondInt=thirdInt
            thirdInt=0
        return secondInt

print lucas(0)

def sum_series(n,indexZero=0,indexOne=1):
    """Take an int 'n', and the first two values in a series, then return the 'nth' value in the sum series"""
    firstInt = indexZero
    secondInt = indexOne

    if n<0:
        return None
    elif int(n)!=float(n):
        return None
    elif n==0:
        return firstInt
    else:
        for i in range(1,n):
            thirdInt = firstInt+secondInt
            firstInt=secondInt
            secondInt=thirdInt
            thirdInt=0
        return secondInt

print sum_series(7)