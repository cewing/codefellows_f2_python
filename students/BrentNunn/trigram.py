#!/usr/bin/env python

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

trigrams = {}
for i in range(len(words) - 3):
    follows = trigrams.setdefault((words[i], words[i + 1]), set())
    follows.add(words[i + 2])

trigram_text = [words[1], words[2]]
for i in range(200):
    choices = list(trigrams[(trigram_text[i], trigram_text[i + 1])])
    next_word = random.choice(choices)
    trigram_text.append(next_word)

for word in trigram_text:
    print word,

