import os
import sys
import string


def trigrams(input_file):
    """Reads a text file and assembles a dict of word level trigrams"""

    # trigram_title = u"Copy a File"
    # print trigram_title
    # print u"-" * len(trigram_title)

    # input_file = raw_input("Enter the name of an existing source file and press Enter: ")
    
    # while input_file is not None:
    #     try:
    #         f = open(input_file)
    #     except IOError:
    #         input_file = raw_input("Source file '%s' does not exist, try again: " % input_file)
    #     else:
    #         break

    # Open the input file for reading
    f = open(input_file, 'r')

    word_list = []
    word_string = ''

    for line in f:
        word_string = word_string + line

    word_string = word_string.lower()

    for p in string.punctuation:
        word_string = word_string.replace(p, ' ')
    
    print word_string

    for word in word_string.split():
        word_list.append(word)

    print word_list

if __name__ == '__main__':
    input_file = sys.argv[1]
    print u""
    trigrams(input_file)