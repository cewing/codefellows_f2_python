def fibonacci(n):
    """return nth value in fibonacci series"""
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        series = [0,1]
        for i in range(2, n):
            series.append(series[i-1] + series[i-2])
        return series[n-1]


def lucas(n):
    """return nth value in lucas series"""
    if n <= 0:
        return None
    elif n == 1:
        return 2
    else:
        series = [2,1]
        for i in range(2, n):
            series.append(series[i-1] + series[i-2])
        return series[n-1]        

def sum_series(n, x = 0, y = 1):
    """return nth value in fibonacci or lucas series or undefined series message"""
    if n < 1:
        return None
    elif n == 1:
        return x
    elif n == 2:
        return y
    else:
        series = [x,y]
        for i in range(2, n):
            series.append(series[i-1] + series[i-2])
        return series[n-1]   
        
    
    
if __name__ == "__main__":
    fib = [0, 1, 1, 2, 3, 5, 8, 13]
    luc = [2, 1, 3, 4, 7, 11, 18, 29]
    #testing fibonacci series with positive numbers
    for i, val in enumerate(fib, start=1):
        assert val == fibonacci(i)
    #testing fibonacci series with nagative numbers and 0
    for n in range (-1, 0):
        assert fibonacci(n) == None
    #testing lucas series with positive numbers
    for i, val in enumerate(luc, start=1):
        assert val == lucas(i)
    #testing lucas series with nagative numbers and 0
    for n in range (-1, 0):
        assert lucas(n) == None
    #testing sum_series with positive numbers
    for i, val in enumerate(fib, start=1):
        assert val == sum_series(i)
    for i, val in enumerate(luc, start=1):
        assert val == sum_series(i, 2, 1)  
    print "All Tests Pass" 
