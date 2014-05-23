#!/usr/bin/env python
import codecs
import random


def trigram(in_file, out_file):
    """Export file by generating text from trigram algorithm from input"""
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

    # Build dictionary of trigrams
    tri_dict = {}
    for i in range(len(all_words) - 2):
        key_words = '%s %s' % (all_words[i], all_words[i + 1])
        tri_dict.setdefault(key_words, [])
        tri_dict[key_words].append(all_words[i + 2])

    # Output some text
    # Pick a random key to start
    words = random.choice(tri_dict.keys())
    out_lines = words
    while True:
        try:
            # Get list of words corresponding to last out_words as key
            # Then pop so we don't reuse
            new_word = tri_dict[words].pop()
            out_lines = '{} {}'.format(out_lines, new_word)
            words = '{} {}'.format(words.split()[1], new_word)
        except KeyError:
            break
    write_file = codecs.open(out_file, 'w')
    write_file.write(out_lines)
