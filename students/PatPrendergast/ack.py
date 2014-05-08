# ack.py


def ack(m, n):
    """Computes the Ackermann function - A(m, n)"""
    
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))

print ack(0, 0)
print ack(1, 0)
print ack(2, 0)
print ack(3, 0)
print ack(4, 0)
print ack(1, 1)


if __name__ == '__main__':
    ''' Testing the Ack function with Assert/Try '''    
    good_acker = [
        ((0, 1), 2), 
        ((1, 0), 2),
        ((1, 1), 3),
        ((1, 2), 4),
        ((2, 2), 7),
        #((2, 3), 9),
        #((0, 3), 4),
        #((1, 4), 6), 
        #((2, 0), 3),
        #((3, 0), 5),
        #((4, 0), 13),
    ]

    bad_acker = [
        ['a', [2,3,4], 5],

    ]

    for input, output in good_acker:
        assert ack(*input) == output
'''
    for input in bad_acker:
        try:
            result = ack(*input) == bad_acker[2]
        except ValueError:
            pass
        else:
            print u"a bad value did not raise the expected error"
            assert(False)
'''

    print "All tests pass"
