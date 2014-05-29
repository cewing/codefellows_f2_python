#!/usr/bin/python


import os


def printpathfiles():
    path = os.path.abspath(os.curdir)
    files = [f for f in os.listdir(os.curdir) if os.path.isfile(f)]
    for f in files:
        print path+"/"+f

if __name__ == '__main__':
    printpathfiles()