import time

class Timer(object):
    """from Doug Hellmann, PyMOTW
    http://pymotw.com/2/contextlib/#module-contextlib
    """
    def __init__(self):
        self.start_time=time.time()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print "This code took %s" %(time.time()-self.start_time)
        return self


def prime(limit):
    num = 2
    while num<limit:
        for i in xrange(2,num+1):
            if i**2>num:
                yield num
                break
            elif num%i==0:  break
        num+=1


with Timer() as foo:
    for i in prime(900000):
        a = i**22

