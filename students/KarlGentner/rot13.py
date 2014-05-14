import string


def rot13(text):
    upAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowAlpha = "abcdefghijklmnopqrstuvwxyz"
    # Rotate alphabet by 13
    upAlphaRot = upAlpha[13:] + upAlpha[:13]
    lowAlphaRot = lowAlpha[13:] + lowAlpha[:13]
    # Make a mapping using string.maketrans(from, to)
    upSwap = string.maketrans(upAlpha, upAlphaRot)
    lowSwap = string.maketrans(lowAlpha, lowAlphaRot)
    # Translate text using mapping
    result = text.translate(upSwap)
    result = result.translate(lowSwap)
    return result


# testing - wondering if there is a better way to do this?
if __name__ == '__main__':
    upAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowAlpha = "abcdefghijklmnopqrstuvwxyz"
    upAlphaRot = upAlpha[13:] + upAlpha[:13]
    lowAlphaRot = lowAlpha[13:] + lowAlpha[:13]
    assert rot13(upAlpha) == upAlphaRot
    assert rot13(lowAlpha) == lowAlphaRot
    assert rot13("1234567890 !@#$%^&*()") == "1234567890 !@#$%^&*()"
    print "All Tests Pass"
