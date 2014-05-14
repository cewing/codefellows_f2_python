# ack.py


def ack(m, n):
    """Computes the Ackermann function - A(m, n)"""
    
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))


if __name__ == '__main__':
    ''' Testing the Ack function with Assert/Try '''    
    good_acker = [
        ((0, 0), 1),
        ((0, 1), 2),
        ((0, 2), 3),
        ((0, 3), 4),
        ((0, 4), 5),
        ((1, 0), 2),
        ((1, 1), 3),
        ((1, 2), 4),
        ((1, 3), 5),
        ((1, 4), 6),
        ((2, 0), 3),
        ((2, 1), 5),
        ((2, 2), 7),
        ((2, 3), 9),
        ((2, 4), 11),
        ((3, 0), 5),
        ((3, 1), 13),
        ((3, 2), 29),
        ((3, 3), 61),
        ((3, 4), 125),
    ]

    bad_acker = [((3.2, -2), 5),]

    for input, output in good_acker:
        assert ack(*input) == output
    
    for e in bad_acker:
        try:
            result = ack(e)
        except TypeError:
            pass
        else:
            print u"a bad value did not raise the expected error"
                   
    print "All tests pass"


    
