"""ROT13--Encoding Messages"""

def rot13(msg):
    """A function to encode text with the Ceaser-cypher."""

    """
    Encodes a given message by shifting the letters 13 spaces but leaving
    and ignoring whitespace.
    """

    return msg.encode('rot13')

if __name__ == '__main__':
    msg = "I do not like green eggs and ham. I do not like them sam-I-am."
    encoded_msg = rot13(msg)
    print u"Original message: " + msg
    print u"Encoded message: " + encoded_msg
    print u"Assertion testing using rot13(rot13())..."

    assert rot13(encoded_msg) == msg
    print "Test passed!"

