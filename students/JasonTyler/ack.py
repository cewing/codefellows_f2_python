"""Ackermann Function Assignment"""


def ackermann(m, n):
    """
    Evaluate the Ackermann function for given integer indexes m, n.

    More information available at
    http://en.wikipedia.org/wiki/Ackermann_function
    Note that tail recursion is a problem, and as written, this function
    can't be evaluated past m = 3, n = 3.
    """

    if not isinstance(m, int) or not isinstance(n, int):
        return None
    elif m < 0 or n < 0:
        return None
    elif m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))


if __name__ == "__main__":
    """Test Ackermann function"""

    ack_vals = [
        [0, 0, 1],
        [0, 1, 2],
        [0, 2, 3],
        [0, 3, 4],
        [0, 4, 5],
        [1, 0, 2],
        [1, 1, 3],
        [1, 2, 4],
        [1, 4, 6],
        [2, 0, 3],
        [2, 1, 5],
        [2, 2, 7],
        [2, 3, 9],
        [2, 4, 11],
        [3, 0, 5],
        [3, 1, 13],
        [3, 2, 29],
        [3, 3, 61],
        [3, 4, 125]
    ]

    ack_rubbish = [
        [1.2, 2, None],
        ["asdfasdf", 3, None],
        [2, 0.2, None],
        [-4, 2, None],
    ]

    def assert_ackermann():
        """Use known output as well as rubbish input to test ackermann()."""
        for output_set in ack_vals:
            assert ackermann(output_set[0], output_set[1]) == output_set[2]
        for output_set in ack_rubbish:
            assert ackermann(output_set[0], output_set[1]) == output_set[2]
        print "Ackermann tests pass ok."

    # calling defined test function
    assert_ackermann()
