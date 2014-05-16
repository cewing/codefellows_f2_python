"""Mathematical Series: Sum"""

def sum_series(n, x=0, y=1):
    """
    This is the basic algorithm for a sum series.

    n will determine the value to return
    x is an optional variable with default for Fibonacci that determines the
        first integer to start the series.
    y is an optional variable with default for Fibonacci that determines the
        second integer to start the series.
    """

    for i in range(n-2):
        newValue = x + y
        x = y
        y = newValue
    return y

def fibonacci(n):
    """Use sum_series function to return Fibonacci value."""
    #default values in sum_series are for fibonacci
    return sum_series(n)

def lucas(n):
    """use sum_series function to return Lucas value."""
    #add starting integer values for x, y
    return sum_series(n, 2, 1)

if __name__ == "__main__":
    """Assertion Tests for the function."""
    #Test Table for Fibonacci sum_series
    fib_table = [1, 2, 3, 5, 8,
                 13, 21, 34, 55, 89,
                 144, 233, 377, 610, 987,
                 1597, 2584, 4181, 6765, 10946]

    #Test Table for Lucas numbers
    luc_table = [3, 4, 7, 11, 18,
                 29, 47, 76, 123, 199,
                 322, 521, 843, 1364, 2207,
                 3571, 5778, 9349, 15127, 24476]

    #Test Table for sum_series random, x = 5, y = 5
    rnd_table = [10, 15, 25, 40, 65,
                 105, 170, 275, 445, 720,
                 1165, 1885, 3050, 4935, 7985,
                 12920, 20905, 33825, 54730, 88555]

    #Assertion test for Fibonacci numbers
    count = 0
    for i in range(20):
        #Must add 3 to i to account for starting range of 0 and n-2 in function
        assert(fibonacci(i+3) == fib_table[count])
        count += 1

    print "Fibonacci numbers passed."

    #Assertion test for Lucas numbers
    count = 0
    for i in range(20):
        #Must add 3 to i to account for starting range of 0 and n-2 in function
        assert(lucas(i+3) == luc_table[count])
        count += 1

    print "Lucas numbers passed."

    #Assertion test for sum_series random numbers
    count = 0
    for i in range(20):
        #Must add 3 to i to account for starting range of 0 and n-2 in function
        assert(sum_series(i+3, 5, 5) == rnd_table[count])
        count += 1

    print "Sum series numbers passed."
