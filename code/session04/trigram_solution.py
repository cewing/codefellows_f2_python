#!/usr/bin/env python

"""
Trigram.py

A solution to the trigram coding Kata:

http://codekata.pragprog.com/2007/01/kata_fourteen_t.html

Chris Barker's Solution
"""

# infilename = "sherlock_small.txt"
infilename = "sherlock.txt"

import string
import random

# translation table for string.translate:
# I use this to purge the punctuation..
# there are other ways to do this -- 
#   a_word.strip() works well, too.   

# stuff I want to keep:
valid = string.letters + "'" # keep the contractions
all = ''.join([chr(i) for i in range(256)])

table = [ c if c in valid else ' ' for c in all]
table = ''.join(table)


infile = open(infilename, 'r')
# strip out the header, table of contents, etc.
for i in range(61):
    infile.readline()

# read the rest of the file into memory
in_data = infile.read()

# Dictionary for trigram results:
# The keys will be all the word pairs
# The values will be a list of the words that follow each pair
word_pairs = {}

# lower-case everything to remove that complication:
in_data = in_data.lower()

# strip out the punctuation:
in_data = in_data.translate(table)

# split into words
words = in_data.split()

# remove the bare single quotes
# " ' " is both a quote and an apostrophe
words = [word for word in words if word != "'"]

# loop through the words
for i in range(len(words) - 2):
    pair = tuple( words[i:i+2] ) # a tuple so it can be a key in the dict
    follower = words[i+2]
    word_pairs.setdefault(pair,[]).append(follower)

    # setdefault() returns the value if pair is already in the dict
    #    if it's not, it adds it, setting the value to a an empty list 
    #    then it returns the list, which we then append the following
    #    word to -- cleaner than:
    # if pair in word_pairs:
    #     word_pairs[pair].append(follower)
    # else:
    #     word_pairs[pair] = [follower]


# A little reporting for testing
#for pair, followers in word_pairs.items():
#    if len(followers) > 1:
#        print pair, followers

# create some new text
new_text = []        
for i in range (100): # do 100 sets.
    pair = random.sample(word_pairs, 1)[0] # random.sample returns a list
    follower = random.sample(word_pairs[pair], 1)[0]
    new_text.extend( (" ".join(pair), follower) )

new_text = " ".join(new_text)

print new_text

