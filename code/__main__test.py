#!/usr/bin/env python

"""
demo of the: if __name__ == '__main__' clause
"""


print "running module: __main___test.py ---- "

print "__name__ is", __name__

if __name__ == '__main__':
    print "Now running code in the __main__ clause"
    # some test or example code here

    result = raw_input("Say Something!")

    print "you said:", result

else:
    print "not running as __main__"
