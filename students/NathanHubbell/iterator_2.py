#!/usr/bin/env python

"""
Simple iterator examples
"""

class IterateMe_2(object):
    """
    A little lesss simple than the simplest iterator.
    """
    def __init__(self, start=0, stop=5, step=1):
        self.current = start-step
        self.stop = stop
        self.step = step
        self.start = start
    def __iter__(self):
        #one solution:
        #self.current=self.start-self.step
        #return self

        #another solution:
        return IterateMe_2(self.start,self.stop,self.step)

    def next(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


it = IterateMe_2(2, 20, 2)
for i in it:
    if i > 10:  break
    print i

for i in it:
    print i

print "---------------"

itx = xrange(2, 20, 2)
for ix in itx:
    if ix > 10:  break
    print ix

for ix in itx:
    print ix
