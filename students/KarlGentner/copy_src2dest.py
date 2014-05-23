#!/usr/bin/python

import sys


src = sys.argv[1]
dest = sys.argv[2]


def copy_src2dest(src, dest):

    src = open(src)
    dest = open(dest, 'w')

    content = src.read()
    dest.write(content)

    src.close()
    dest.close()


if __name__ == '__main__':
    copy_src2dest(src, dest)