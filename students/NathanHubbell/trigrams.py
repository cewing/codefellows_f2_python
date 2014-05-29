#!/usr/bin/env python
import codecs, os, sys, string, random
table = string.maketrans("","")
trigramfirst = {}
readfile = codecs.open('kipling.txt','r')

def makeOutput(firstWord,secondWord):
    try:
        nextword = trigramfirst["%s %s"%(firstWord,secondWord)]
        randomword= random.choice(nextword)
        return randomword
    except KeyError:
        print "This is the end."
    except RuntimeError:
        print "an endless loop an endless loop an..."


def readChunk():
    return readfile.read(10000)


def fillDictionary(trigramfirst):
    for piece in iter(readChunk, ''):
        wordlist = piece.translate(table,string.punctuation).lower().strip().split()
        for i in range(2,len(wordlist)):
            twoWords="%s %s"%(wordlist[i-2],wordlist[i-1])
            followingWord=wordlist[i]
            if twoWords not in trigramfirst:
                trigramfirst[twoWords] = [followingWord]
            else:
                trigramfirst[twoWords].append(followingWord)


###MAIN BODY###
fillDictionary(trigramfirst)
firstWord,secondWord=u"too",u"much"
result = firstWord
for i in range(50):
    result="%s %s"%(result,secondWord)
    firstWord,secondWord = secondWord,makeOutput(firstWord,secondWord)
print result
