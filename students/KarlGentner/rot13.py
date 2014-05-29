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
