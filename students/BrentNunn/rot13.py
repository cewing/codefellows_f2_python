#!/usr/bin/env python

import string

def rot13(text):
    """Return the text after ROT13 encryption."""

    trans_from = u"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    trans_to = u"NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    trans_tbl = string.maketrans(trans_from, trans_to)

    return text.translate(trans_tbl)
    #return "Hey! Is this the way to San Jose?".translate(trans_tbl)


if __name__ == '__main__':
    print u"Testing ROT13 implementation."

    test_string1 = u"Hey! Is this the way to San Jose?"
    encrypted = rot13(test_string1)

    print u"Before encryption: {}".format(test_string1)
    print u"After encryption:  {}".format(encrypted)

    print u"'A' after encrpytion = {}".format(rot13(u"A"))

    #assert ord(rot13(u"A")) == ord(u"A") + 13
    #assert ord(rot13(u"a")) == ord(u"a") + 13


