#!/usr/bin/env python
"""Code Fellows Functional Files assignment"""

import codecs
import sys


if __name__ == '__main__':
    print u"\nCode Fellows Functional Files assignment, map version."

    if len(sys.argv) < 3:
        print (u"Usage: functional_files_map.py "
               u"<source_text_file> <destination_file>\n"
               u"Leading and trailing spaces will be stripped from "
               u"each line of text in the source_text_file."
               u"If both file names are the same then the file "
               u"will be replaced with the results.\n"
              )
        exit()

    with codecs.open(sys.argv[1]) as source_file:
        source_content = source_file.read()

    map_list = map(lambda line: line.strip() + '\n', 
                   source_content.splitlines())

    with codecs.open(sys.argv[2], 'w') as dest_file:
        for line in map_list:
            dest_file.write(line)
        

    
