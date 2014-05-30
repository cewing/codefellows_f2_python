#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class IterateMe_2(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, start, stop, step=1):
        self.start = start
        self.current = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return IterateMe_2(self.start, self.stop, self.step)

    def next(self):
        self.current += 1 * self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print "first version"
    for i in IterateMe_1():
        print i

    print "second version"
    for i in IterateMe_2(2, 20, 2):
        print i

    print "xrange"
    for i in xrange(2, 20, 2):
        print i

    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10: break

    assert [i for i in it] == [2, 4, 6, 8, 10, 12, 14, 16, 18]

    print "xrange test passed"
