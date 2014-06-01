import time

class Timer(object):
    """A context manager that prints the elapsed run time"""


    def __init__(self):
        pass


    def __enter__(self):

        # Get the starttime
        self.start_time = time.time()
        # print self.start_time

        return self


    def __exit__(self, exc_type, exc_val, exc_tb):

        # Get the end time
        self.end_time = time.time()
        # print self.start_time
        # print self.end_time

        # Calculate and print the elapsed time
        self.elapsed_time = self.end_time - self.start_time
        print u"This code took {0} seconds.".format(self.elapsed_time)


if __name__ == '__main__':

    with Timer() as t:
        for i in range(100000):
            i = i ** 20