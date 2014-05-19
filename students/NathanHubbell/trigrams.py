#!/usr/bin/env python
import codecs, os, sys, string
table = string.maketrans("","")
trigramfirst = {"two words":["aword","anotherword","aword"]}
trigramDictTwoWords = {"two words":{"followingword":1,"anotherFollowingWord":5}}
readfile = codecs.open('HOLMES.txt','r')
lineCount=0
number_of_lines=50
for aline in readfile:
    lineCount=lineCount+1
    if lineCount == number_of_lines:
        break
    cleanLine = aline.translate(table,string.punctuation).lower().strip()
    wordlist = cleanLine.split(" ")
    for i in range(2,len(wordlist)):
        trigramfirst.update({"%s %s"%(wordlist[i-2],wordlist[i-1]):wordlist[i]})
print trigramfirst



