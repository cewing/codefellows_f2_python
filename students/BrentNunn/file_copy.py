#!/usr/bin/env python

import sys

if len(sys.argv) <> 3:
    print 'usage: file_copy.py <source_file> <dest_file>'
    exit()

f1 = open(sys.argv[1])
f2 = open(sys.argv[2], 'w')

f2.write(f1.read())    
