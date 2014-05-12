"""Ackerman's Function"""

def ack(m, n):

    """
    Evaluate Ackerman's Function.

    This function is recursive and can only be used for m <= 3 and
    n <= 3.
    """

    if not (isinstance(m, int) and m >= 0) or not (isinstance(n, int) and n >= 0):
        return None

    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        ack(m-1, 1)
    else:
        ack(m-1, ack(m, n-1))


#if __name__ == "__main__":
#
#    """Assertion testing for Ackerman's Function"""