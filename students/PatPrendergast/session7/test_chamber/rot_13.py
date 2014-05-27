#!/usr/bin/env python

# CAPS VALUES = ORD 65 - 90, LOWER VALUES = ORD 97 - 122
# ord('A'), ord('Z') & ord('a'), ord('z')


#Create lists for indexing the letter ord values
cap_vals = range(65, 91)
cap_vals_offset = range(78, 91) + range(65, 78)
lower_vals = range(97, 123)
lower_vals_offset = range(110, 123) + range(97, 110)


def rot_13(word):
    u''' Offsets letters by 13 using list index references '''
    result = ''
    for letter in word:
        letter = ord(letter)
        if letter in cap_vals:
            i = cap_vals.index(letter)
            letter = cap_vals_offset[i]
        elif letter in lower_vals:
            i = lower_vals.index(letter)
            letter = lower_vals_offset[i]
        result += chr(letter)
    return result

