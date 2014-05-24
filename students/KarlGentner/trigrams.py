#!/usr/bin/python

import sys
import codecs
import string


# Given some text, removes punctuation and returns a dictionary of  word-level trigrams
def createTrigramDict(text):
    # Make a mapping of punctuation to space using string.maketrans(from, to)
    punc_to_space = string.maketrans(string.punctuation, ' '*len(string.punctuation))
    # Translate text using mapping
    text = text.translate(punc_to_space)
    # Create a list of words in original text order
    words = text.split()
    # In a dictionary, fill keys and values with word-level trigrams
    d = {}
    for i in range(len(words)-2):
        key = words[i] + " " + words[i+1]
        value = words[i+2]
        if key in d:
            d[key].append(value)
        else:
            d[key] = [value]
    return d


# Given a dictionary 'd' of word-level trigrams, returns new word ordering in a list.
def reorderTrigramWords(d):
    startingTrigram = d.popitem()
    startingText = "{key} {value}".format(key=startingTrigram[0].capitalize(), value=startingTrigram[1][0])
    wordlist = startingText.split()
    nextKey = wordlist[len(wordlist)-2] + " " + wordlist[len(wordlist)-1]
    # Fill the rest of words list
    while nextKey in d:
        # "Get" 1 value if key has more than 1 in value it's list, OR "pop" value if its the only one
        if len(d.get(nextKey)) > 1:
            nextWord = d.get(nextKey).pop(1)
        else:
            nextWord = d.pop(nextKey)[0]
        # Add nextWord to wordlist
        wordlist.append(nextWord)
        nextKey = wordlist[len(wordlist)-2] + " " + wordlist[len(wordlist)-1]
    return wordlist


# Given a list of words, returns altered text with inserted periods and paragraphs.
def formatAlteredText(wordlist):
    altText = wordlist.pop(0)
    sentenceCount = 0
    wordCount = 0
    for i in range(len(wordlist)-1):
        altText += " " + wordlist[i]
        wordCount += 1
        # if the next word is capitalized and current sentence is at least 4 words, add a period and start a new sentence
        if not wordlist[i+1].islower() and wordCount > 4:
            altText += "."
            wordCount = 0
            sentenceCount += 1
            # after 12 sentences, start a new paragraph
            if sentenceCount % 12 == 0:
                altText += "\n\n"
    return altText


if __name__ == '__main__':
    filename = sys.argv[1]
    f = codecs.open(filename)
    text = f.read()
    f.close()
    d = createTrigramDict(text)
    wordlist = reorderTrigramWords(d)
    altText = formatAlteredText(wordlist)
    print altText