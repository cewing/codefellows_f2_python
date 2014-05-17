#!/usr/bin/env python

def rot13(text):
    """Return the text after ROT13 encryption."""

    text_encrypted = ""

    for ch in text:
        if ch >= 'A' and ch <= 'Z':
            rot13_ch = ord(ch) + 13
            if rot13_ch > ord('Z'):
                rot13_ch = ord('A') + rot13_ch - ord('Z') - 1

            text_encrypted += chr(rot13_ch)

        elif ch >= 'a' and ch <= 'z':
            rot13_ch = ord(ch) + 13
            if rot13_ch > ord('z'):
                rot13_ch = ord('a') + rot13_ch - ord('z') - 1

            text_encrypted += chr(rot13_ch)

        else:
            text_encrypted += ch


    return text_encrypted


if __name__ == '__main__':
    print u"Testing ROT13 implementation."

    test_string1 = u"Hey! Is this the way to San Jose?"
    encrypted = rot13(test_string1)

    print u"Before encryption: {}".format(test_string1)
    print u"After encryption:  {}".format(encrypted)

    print u"'A' after encryption = '{}'".format(rot13(u"A"))
    print u"'Z' after encryption = '{}'".format(rot13(u"Z"))
    print u"'a' after encryption = '{}'".format(rot13(u"a"))
    print u"'z' after encryption = '{}'".format(rot13(u"z"))

    assert ord(rot13(u"A")) == ord(u"A") + 13
    assert ord(rot13(u"Z")) == ord(u"A") + 12
    assert ord(rot13(u"a")) == ord(u"a") + 13
    assert ord(rot13(u"z")) == ord(u"a") + 12


