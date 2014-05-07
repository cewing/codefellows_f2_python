import sys

def fibonacci(n):
    """This function returns the nth value of the Fibonacci sequence"""

    # Convert input to int, in case a negative integer is passed in
    n = int(n)
    
    # First two value of sequence are fixed at 0 and 1, so just return them if they're passed in
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        print fibonacci(n-2), type(fibonacci(n-2))
        print fibonacci(n-1), type(fibonacci(n-1))
        # fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    n = sys.argv[1]
    fibonacci(n)