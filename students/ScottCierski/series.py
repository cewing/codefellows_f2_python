import sys

def fibonacci(n):
    """This function returns the nth value of the Fibonacci sequence"""

    # Convert input to int, in case a negative integer is passed in
    n = int(n)

    a = 0
    b = 1

    if n < 0:
        print('Only positive values are allowed.')
        return None
    # First two values of sequence are fixed at 0 and 1, so just return them if they're passed in
    elif n ==0:
        return 0
    elif n ==1:
        return 1
    # This is a special case hack for 2
    elif n == 2:
        return a + b
    else:
        for i in range(n-2):
            # add current two values
            c = a + b

            # Debugging
            # print '1st: ', a, b, c

            # Shift b and c back to a and b 
            a = b
            b = c

            # Debugging
            print '2nd: ', a, b

    return b

if __name__ == '__main__':
    n = sys.argv[1]
    fibonacci(n)