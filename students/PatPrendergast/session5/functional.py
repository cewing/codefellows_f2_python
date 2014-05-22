# functional.property
import string

def get_file(filename):
    
    try:
        fop = open(filename, 'r')
        contents = fop.readlines()
    except:
        print "No file found"
        return 
    contents = map(str.strip, contents)
    return contents

def write_to(word_list, filename):
    write_to = raw_input(u'''Writing to a file...
Do you wish to overwrite the original file? Y or N>''')
    if write_to == u'Y' or write_to == u'y':
        fop = open(filename, 'w')
        for line in word_list:
            fop.write(line)
        fop.close()

    else:
        new_file = raw_input('What file (filename) will be written to: >')
        fop = open(new_file, 'w')
        for line in word_list:
            fop.write(line)
        fop.close()

filename = raw_input(u'What file do you wish to open?')
contents = get_file(filename)
write_to(contents, filename)



