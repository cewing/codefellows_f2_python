import string

def rot13():
    """Perform ROT13 encryption"""

    input_string = raw_input('Please enter a string: ')
    print u""

    translate_table = string.maketrans( "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

    rot_13_input_string = string.translate(input_string, translate_table)

    print u"Printing ROT13 for this string..."
    print rot_13_input_string
    print u""

if __name__ == '__main__':
    rot13()