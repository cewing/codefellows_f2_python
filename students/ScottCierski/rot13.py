import string

def rot13(input_string):
    """Perform ROT13 encryption"""

    translate_table = string.maketrans( "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

    rot_13_input_string = string.translate(input_string, translate_table)
    return rot_13_input_string

if __name__ == '__main__':

    # Assert block
    # Test all lower case
    assert rot13('amq') == 'nzd'

    # Test all upper case
    assert rot13('BGW') == 'OTJ'

    # Test mix of lower case, upper case
    assert rot13('fRx') == 'sEk'

    # Test mix of lower case, upper case, numbers
    assert rot13('J5oL8') == 'W5bY8'

    # Test mix of lower case, upper case, numbers, white space, special characters
    assert rot13('dS 4e!T @y*') == 'qF 4r!G @l*'

    # Accept user input
    input_string = raw_input('Please enter a string: ')
    print u""

    print u"Printing ROT13 for this string..."
    rot_13_input_string = rot13(input_string)
    print rot_13_input_string