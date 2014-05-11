from string import maketrans

_char_uncrypt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_char_crypt = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
_rot13trans = maketrans(_char_uncrypt, _char_crypt)
_rot13decrypttrans = maketrans(_char_uncrypt, _char_crypt)


def rot13(in_str):
    """Encrypt text using ROT13 scheme."""
    return in_str.translate(_rot13trans)


if __name__ == "__main__":
    test_text = "How can you tell an extrovert from an introvert at NSA?\
                 Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf."
