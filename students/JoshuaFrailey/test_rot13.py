import rot13
import string


def test_upper():
    assert rot13.rot13("A") == "N"


def test_lower():
    assert rot13.rot13("a") == "n"


def test_punctuation():
    for punc in string.punctuation:
        assert rot13.rot13(punc) == punc


def test_phrase():
    assert rot13.rot13("Hello world!") == "Uryyb jbeyq!"
