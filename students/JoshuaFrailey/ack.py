def ack(m, n):
    """Return the Ackermann-Peter function.

    Arguments:
    m: A nonnegative integer between 0 and 3 inclusive.
    n: A nonnegative integer between 0 and 4 inclusive.
    Return value: A nonnegative integer
    """
    if (not isinstance(m, int)) or (not isinstance(n, int)):
        raise ValueError
    if (m < 0) or (n < 0):
        raise ValueError
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

    for input_ in vals:
        assert ack(input_[0], input_[1]) == vals[input_]

    badvals = [
        (-1, -1),
        (-1, -3.14),
        (-1, 2.78),
        (-1, 'a'),
        (-1, []),
        ('a', -1),
        ('a', -3.14),
        ('a', 2.78),
        ('a', 'a'),
        ('a', []),
        (2.78, -1),
        (2.78, -3.14),
        (2.78, 2.78),
        (2.78, 'a'),
        (2.78, [])
        ]

    for badval in badvals:
        try:
            result = ack(badval[0], badval[1])
        except ValueError:
            pass
        else:
            print u"A bad value did not trigger a ValueError"

    print u"All tests passed!"