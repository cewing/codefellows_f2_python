#!/usr/bin/env python
"""Generate a trigram from text, and print some of the generated output"""

import codecs
import random

try:
    #f = codecs.open('sherlock_small.txt', 'U')
    f = codecs.open('sherlock.txt', 'U')
except Exception, e:
    print 'Missing input file'
    raise
else:
    text = f.read()
finally:
    f.close()

words = text.split()

#Create a dictionary of trigrams, 2 word tuples as keys, and a list
# of words that follow those 2 words in the text
trigrams = {}
for i in range(len(words) - 3):
    follows = trigrams.setdefault((words[i], words[i + 1]), set())
    follows.add(words[i + 2])

#Use the trigrams generated above to build a new list of words.
#The first 2 words match the input text, for improved readability.
trigram_text = [words[1], words[2]]
i = 0
while True:
    choices = list(trigrams[(trigram_text[i], trigram_text[i + 1])])
    #End if by chance the last pair of generated words were not in a trigram
    if len(choices) == 0:
        break

    next_word = random.choice(choices)
    trigram_text.append(next_word)
    i += 1
    if i >= 200:
        #After 200 words, we want the output to end on the next period
        if next_word.count('.'):
            break

for word in trigram_text:
    print word,
print ""
