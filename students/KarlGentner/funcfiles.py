#!/usr/bin/python
import sys
import codecs


filename = sys.argv[1]


def cleanLines(filename):
    # Create list of cleaned lines using map
    f = codecs.open(filename)
    lineListMap = map(lambda line: line.strip(), f)
    print lineListMap
    # Create list of cleaned lines using list comprehension
    f = codecs.open(filename)
    lineListComp = [line.strip() for line in f]
    print lineListComp


if __name__ == '__main__':
    cleanLines(filename)
