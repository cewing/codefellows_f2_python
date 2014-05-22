#!/usr/bin/env python
import codecs


def trigram(in_file):
    orig = codecs.open(in_file)
    # Strip whitespace and new lines
    orig_lines = map(str.strip, orig.readlines())
    # Split into individual words
    orig_words = map(str.split, orig_lines)
    # Make 1 list
    all_words = []
    for line in orig_words:
        for word in line:
            all_words.append(word)
    print all_words
