# ack.py - Karl Gentner - CFF2 Python


def ack(m, n):
    """Return the value of Ackermann's function"""
    if m < 0 or n < 0:
        return None
    elif m == 0:
        return n + 1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

# test
if __name__ == '__main__':
    ackTable = ((1, 2, 3, 4), (2, 3, 4, 5), (3, 5, 7, 9), (5, 13, 29, 61))
    for i, x in enumerate(ackTable):
        for j, y in enumerate(x):
            assert ack(i, j) == y
    print "All Tests Pass"
