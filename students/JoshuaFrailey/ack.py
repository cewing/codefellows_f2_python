def ack(m, n):
    """Return the Ackermann-Peter function.


    m: a nonnegative integer between 0 and 3 inclusive.
    n: a nonnegative integer between 0 and 4 inclusive.
    """
    if m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

if __name__ == '__main__':
    vals = {
        (0, 0): 1,
        (0, 1): 2,
        (0, 2): 3,
        (0, 3): 4,
        (0, 4): 5,
        (1, 0): 2,
        (1, 1): 3,
        (1, 2): 4,
        (1, 3): 5,
        (1, 4): 6,
        (2, 0): 3,
        (2, 1): 5,
        (2, 2): 7,
        (2, 3): 9,
        (2, 4): 11,
        (3, 0): 5,
        (3, 1): 13,
        (3, 2): 29,
        (3, 3): 61,
        (3, 4): 125,
        }
