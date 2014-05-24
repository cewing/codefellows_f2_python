#!/usr/bin/env python
"""Trigrams assignment"""
import re
import random


test_fragment = """
One night--it was on the twentieth of March, 1888--I was
returning from a journey to a patient (for I had now returned to
civil practice), when my way led me through Baker Street. As I
passed the well-remembered door, which must always be associated
in my mind with my wooing, and with the dark incidents of the
Study in Scarlet, I was seized with a keen desire to see Holmes
again, and to know how he was employing his extraordinary powers.
His rooms were brilliantly lit, and, even as I looked up, I saw
his tall, spare figure pass twice in a dark silhouette against
the blind. He was pacing the room swiftly, eagerly, with his head
sunk upon his chest and his hands clasped behind him. To me, who
knew his every mood and habit, his attitude and manner told their
own story. He was at work again. He had risen out of his
drug-created dreams and was hot upon the scent of some new
problem. I rang the bell and was shown up to the chamber which
had formerly been in part my own.
"""


wee_test = "one night--it was on the twentieth of March, 1888--I was returning from a journey to a patient"


def generate_trigram_clean(string):
    """
    Generate a trigrams dictionary from a string.

    This particular version ignores punctuation; i.e. it will pick n-grams
    across punctuation boundaries, even if those boundaries are periods marks.
    """
    bits = split_all(string)
    # Clean bits such that it contains only words
    bits = [bit for bit in bits if bit.isalpha()]
    # Generate trigrams from bits list
    trigrams = dict()
    for i in range(len(bits) - 2):
        key = " ".join(bits[i: i + 2])
        try:
            trigrams[key].append(bits[i + 2])
        except KeyError:
            trigrams[key] = []
            trigrams[key].append(bits[i + 2])
    return trigrams


def generate_trigram(string):
    """
    Generate a trigrams dictionary from a string.

    This particular version retains punctuation; i.e. it keys verbatim n-word 
    phrases with adjacent non-whitespace punctuation and returns values that
    may contain ending punctuation as well. 
    """
    bits = string.split()
    trigrams = dict()
    for i in range(len(bits) - 2):
        key = " ".join(bits[i: i + 2])
        try:
            trigrams[key].append(bits[i + 2])
        except KeyError:
            trigrams[key] = []
            trigrams[key].append(bits[i + 2])
    return trigrams


def translate_trigram(string, trigrams):
    """
    Translate a string using a trigram dict
    
    Starting with a version that looks for punctuation-matching keys.
    """
    bits = string.split()
    for i in range(len(bits) - 2):
        key = " ".join(bits[i: i + 2])
        try:
            alternates = trigrams[key]
        except (NameError, KeyError):
            pass
        else:
            bits[i + 2] = random.choice(alternates)
    return " ".join(bits) 


def read_file_as_string(filename):
    with open(filename) as file:
        epic_string = file.read()
    return epic_string 


def split_all(string, retain_whitespace=False):
    """
    Split string such that alpha blocks are isalpha; retain whitespace if True
    
    example
    >>>str = "why, hello?!"
    >>>print split(str)
    ['why', ',', 'hello', '?', '!']
    >>>print str.split() 
    ['why,', 'hello?!']
    """
    if not retain_whitespace:
        return re.findall(r"\w+|[^\w\s]", string, re.UNICODE)
    else:
        return re.findall(r"\w+|[^\w]", string, re.UNICODE)


def update_dictlist(dict1, dict2):
    """Update dict1 in-place using key, values in dict2 if key doesn't yet exist"""
    for key, item in dict2.iteritems():
        if not dict1.has_key(key):
            dict1.setdefault(key, []).extend(item)
        else:
            pass


if __name__ == "__main__":
    # Using sherlock.txt and two methods of generating trigrams to translate test_fragment
    trigrams = generate_trigram(read_file_as_string('sherlock.txt'))
    trigrams2 = generate_trigram_clean(read_file_as_string('sherlock.txt'))
    update_dictlist(trigrams, trigrams2)
    translated_test_fragment = translate_trigram(test_fragment, trigrams)
    print translated_test_fragment

