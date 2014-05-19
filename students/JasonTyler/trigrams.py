"""Trigrams assignment"""

import re

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

trigrams = dict()
def trigram(string):
    bits = split_all(string)
    #print {bit: bit.isalpha() for bit in bits }

    for i in range(len(bits) - 2):
        if bits[i].isalpha():
            if trigrams.has_key(bits[i]):
                trigrams[bits[i]].extend(bits[i + 1: i + 3])
            else:
                trigrams[bits[i]] = list(bits[i + 1: i + 3])


def split_all(string):
    """
    Split a string such that punctuation is separated
    
    >>>str = "why, hello?!"
    >>>print split(str)
    ['why', ',', 'hello', '?', '!']
    >>>print str.split() 
    ['why,', 'hello?!']
    """
    return re.findall(r"\w+|[^\w\s]", string, re.UNICODE)

trigram(wee_test)
print trigrams

new_wee_string = str()
for word in wee_test:
    for i in len(wee_test):
        
