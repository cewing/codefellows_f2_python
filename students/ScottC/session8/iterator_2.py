class IterateMe_2(object):
    """Expanded iterator, returns the sequence of numbers from start to stop, incremented by step)"""
    
    def __init__(self, start, stop, step=1):
        self.current = -1
        self.start = start
        self.stop = stop
        self.step = step


    def __iter__(self):
        #First call reset() to reset the iterator back to its initialized values
        self.reset()
        
        return self


    def next(self):

        self.current += self.step

        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


    # This method allows the iterator to be reset each time __iter__ is called, to mimic the behavior of xrange()
    def reset(self):
        self.current = self.start - self.step


if __name__ == "__main__":
    
    # Set some values for testing
    start = 1
    stop = 20
    step = 1

    # Demonstration Code

    # Run xrange() twice
    print 'xrange run 1'
    xr = xrange(start, stop, step)
    for i in xr:
        if i > 10:  break
        print i
    
    print 'xrange run 2'
    for i in xr:
        print i

    print '+' * 30

    # Now run IterateMe_2 twice, in the exact same manner as the xrange() example
    it = IterateMe_2(start, stop, step)
    print 'IterateMe_2 run 1'
    for i in it:
        if i > 10:  break
        print i

    print 'IterateMe_2 run 2'
    for i in it:
        print i