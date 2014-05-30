#!/usr/bin/env python


def ack(m, n):
    """Return value of Ackermann function"""
    # Make sure m and n are integers
    if not isinstance(m, int) or not isinstance(n, int):
        return None

    if m == 0:
        f = n + 1
    elif m > 0 and n == 0:
        f = ack(m - 1, 1)
    elif m > 0 and n > 0:
        f = ack(m - 1, ack(m, n - 1))
    else:
        # This will include if m or n <0
        return None
    return f
