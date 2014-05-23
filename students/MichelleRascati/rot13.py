def rot13(x):
    """Return ROT13 encrypted text."""
    y = x.encode('rot13')
    return y

if __name__ == '__main__':
    assert rot13(u'The quick brown fox 123!?') == u'Gur dhvpx oebja sbk 123!?'
    print 'All tests pass'
