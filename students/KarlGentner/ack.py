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
