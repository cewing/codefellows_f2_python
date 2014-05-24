#!/usr/bin/env python
"""Generate a trigram from text, and print some of the generated output"""

import codecs
import random
import sys


def get_text(text_file):
    """get a text file and split the contents into a word list"""
    try:
        f = codecs.open(text_file)
    except Exception, e:
        print 'Missing input file'
        raise
    else:
        text = f.read()
    finally:
        f.close()

    words = text.split()
    return words


def generate_trigrams(words):
    """Generate trigrams from a list of words"""
    #Create a dictionary of trigrams, 2 word tuples as keys, and a list
    # of words that follow those 2 words in the text
    trigrams = {}
    for i in range(len(words) - 3):
        follows = trigrams.setdefault((words[i], words[i + 1]), set())
        follows.add(words[i + 2])

    return trigrams


def trigram_output(trigrams, first_words = None, length=200):
    """Create text list based on a trigram dictionary."""
    
    #User has option to "prime" the output with initial list of words, for readability.
    if first_words:
        trigram_text = first_words
    else:
        trigram_text = list(random.choice(trigrams.keys()))

    i = 0
    while True:
        words = list(trigrams[(trigram_text[i], trigram_text[i + 1])])
        #End if by chance the last pair of generated words is not a trigram key
        if len(words) == 0:
            break

        next_word = random.choice(words)
        trigram_text.append(next_word)

        i += 1
        if i >= length:
            #After length reached, we want the output to end on the next period
            if next_word.count('.'):
                break

    return trigram_text


if __name__ == '__main__':
    print u"\nWelcome to trigrams."

    if len(sys.argv) <= 1:
        print 'Usage: trigram.py <text_file>\n'
        exit()

    words = get_text(sys.argv[1])
    trigrams = generate_trigrams(words)
    starting_words = [words[0], words[1]]
    results = trigram_output(trigrams, starting_words, length = 200)
    for word in results:
        print word,
    print ""

    
