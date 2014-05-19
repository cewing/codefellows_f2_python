# functional.property
import string

def get_file():
    filename = raw_input(u'What file do you wish to open?')
    fop = open(filename, 'r')
    contents = fop.readlines()
    for line in contents:
        line.strip(string.whitespace) #Not quite it.
    return contents

def write_to(word_list, outfile=None):
    write_to = raw_input(u'''Writing to a file...
        Do you wish to overwrite the original file? Y or N>''')
    if write_to == u'Y' or write_to == u'y':
        outfile.write(contents)
    else:
        new_file = raw_input('What file (filename) will be written to: >')
        new_file.write(contents)

contents = get_file()
print contents

''' Use map... '''