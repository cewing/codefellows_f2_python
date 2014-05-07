import sys

def fibonacci(n):
    """This function returns the nth value of the Fibonacci sequence"""

    # Convert input to int, in case a negative integer is passed in
    n = int(n)
    
    # Early out if negative integer is passed in 
    if n < 0:
        print('Only positive values are allowed.')
        return None
    # First two value of sequence are fixed at 0 and 1, so just return them if they're passed in
    elif n < 2:
        return n
    else:
        ret = fibonacci(n-2) + fibonacci(n-1)
        print ret

if __name__ == '__main__':
    n = sys.argv[1]
    fibonacci(n)