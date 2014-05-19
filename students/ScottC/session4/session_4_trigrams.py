
# Usage:
# $ python session_4_trigrams.py [-v or --verbose] filename
#
# Use -v or --verbose to see extensive details about what the script is doing at each stage.
#
# Verbose mode is useful for small input files, but may produce an overwhelming amount of 
#       information for large files.
# 
# Recommended uses for teacher evaulation:
# 
# $ python session_4_trigrams.py --verbose wisht.xt
# $ python session_4_trigrams.py --verbose sherlock_small.txt
# $ python session_4_trigrams.py sherlock.txt

import sys
import string


def trigrams(is_verbose, input_file):
    """Reads a text file and assembles a dict of word level trigrams"""

    # Do some basic checking for existence of source file
    while input_file is not None:
        try:
            f = open(input_file)
        except IOError:
            print u"Source file '%s' does not exist, exiting." % (input_file)
            return
        else:
            break

    # Open the input file for reading
    f = open(input_file, 'r')

    # Initialize empty string, empty list, empty dict
    word_string = ''
    word_list = []
    trigram_dict = {}

    # Read fie into string
    for line in f:
        word_string = word_string + line

    # Convert string to all lower case
    word_string = word_string.lower()

    # Strip punctuation from string
    for p in string.punctuation:
        word_string = word_string.replace(p, ' ')
    
    if is_verbose == True:
        word_string_title = u"Here is the complete sanitized word string:"
        print word_string_title
        print u"-" * len(word_string_title)
        print word_string
        print u""

    # Split and load it into list
    for word in word_string.split():
        word_list.append(word)

    if is_verbose == True:
        word_list_title = u"Here is the complete word list:"
        print word_list_title
        print u"-" * len(word_list_title)
        print word_list
        print u""

    # Build a dict of trigrams:
    # The dict key is a tuple of two adjacent words
    # The dict value is a list of the individual words that follow the two words in the key
    # For example, the string "I wish I may I wish I might" results in this dict:
    # {
    # ("I", "wish"): ["I", "I"],
    # ("wish", "I"): ["may", "might"],
    # ("may", "I"): ["wish"],
    # ("I", "may"): ["I"]
    # }

    if is_verbose == True:
        word_groups_title = u"Here are the groups of three words:"
        print word_groups_title
        print u"-" * len(word_groups_title)

    word_1, word_2, word_3 = 0, 1, 2
    while word_1 <= len(word_list) - 3:

        if is_verbose == True:
            print word_list[word_1], word_list[word_2], word_list[word_3]    

        # Use setdefault() to add the two word tuple as a dict key if it doesn't already exist in the dict, or append to the value list if it does exist
        # See example here: https://docs.python.org/2/library/collections.html#collections.defaultdict
        # This is where the magic happens! :D
        trigram_dict.setdefault( (word_list[word_1], word_list[word_2]), [] ).append(word_list[word_3])

        # Increment the words
        word_1 += 1
        word_2 += 1
        word_3 += 1

    if is_verbose == True:
        print u""

    if is_verbose == True:
        trigram_dict_title = u"Here is the complete trigram dict:"
        print trigram_dict_title
        print u"-" * len(trigram_dict_title)
        print trigram_dict
        print u""

    # Print the "interesting" trigrams, i.e. the ones with more than one item in the value list
    print_interesting_trigrams_title = u"Here are the trigrams with more than one word:"
    print print_interesting_trigrams_title
    print u"-" * len(print_interesting_trigrams_title)

    for k, v in trigram_dict.items():
        if len(v) > 1:
            print k, v


if __name__ == '__main__':

    is_verbose = False
    usage_message = u"Usage: $ python session_4_trigrams.py [-v or --verbose] filename"

    # Input checking
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
    elif len(sys.argv) == 3 and (sys.argv[1] == u"-v" or sys.argv[1] == u"--verbose"):
            is_verbose = True
            input_file = sys.argv[2]
    else:
        print usage_message
        quit()

    print u""
    trigrams(is_verbose, input_file)