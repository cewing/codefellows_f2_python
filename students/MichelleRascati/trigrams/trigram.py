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

    tri_dict = {}
    for i in range(len(all_words) - 2):
        key_words = '%s %s' % (all_words[i], all_words[i + 1])
        tri_dict.setdefault(key_words, [])
        tri_dict[key_words].append(all_words[i + 2])

    print tri_dict
