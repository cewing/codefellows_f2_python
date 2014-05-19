#!/usr/bin/env python
import codecs, os, sys, string
table = string.maketrans("","")
trigramfirst = {"two words":["aword","anotherword","aword"]}
trigramDictTwoWords = {"two words":{"followingword":1,"anotherFollowingWord":5}}
readfile = codecs.open('HOLMES.txt','r')


#Generate Dictionary
lineCount=0
number_of_lines=13000
for aline in readfile:
    lineCount=lineCount+1
    if lineCount == number_of_lines:
        break
    cleanLine = aline.translate(table,string.punctuation).lower().strip()
    wordlist = cleanLine.split(" ")
    for i in range(2,len(wordlist)):
        twoWords="%s %s"%(wordlist[i-2],wordlist[i-1])
        followingWord=wordlist[i]
        if twoWords not in trigramfirst:
            trigramfirst[twoWords] = [followingWord]
        else:
            trigramfirst[twoWords].append(followingWord)


finalResult=""

thisCount=0



def makeOutput(start,thisCount):
    nextword = trigramfirst[start]

    start = start.split()
    nextKey = "%s %s"%(start[1],nextword[0])
    print start[1]
    #finalResult = finalResult+nextKey
    thisCount=thisCount+1
    if thisCount < 12:
        makeOutput(nextKey,thisCount)



makeOutput("cleared up",1)