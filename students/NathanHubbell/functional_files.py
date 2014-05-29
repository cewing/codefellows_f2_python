#!/usr/bin/env python
import codecs, os, sys

filename = sys.argv[1]
cwd = os.getcwd()



while True:
    choice=raw_input(u"Would you like to write a new file (1) or write over the old file (2)?")

    if choice == "1":
        print "You chose to create a new file: %s/cleaned_file.txt"%(cwd)
        outfile = codecs.open("%s/cleaned_file.txt"%(cwd),'w')
        for line in codecs.open(filename):
            outfile.write("%s\n"%line.strip())

    if choice == "2":
        print "You chose to write over the old file: %s/%s"%(cwd,filename)
        readfile = codecs.open(filename,'r+')
        readfile.seek(0)
        for line in readfile:
            readfile.write("%s\n"%line.strip())
