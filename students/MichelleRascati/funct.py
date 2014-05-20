import codecs


def funct(f_name):
    """Remove leading and trailing whitespace from file."""
    f_read = codecs.open(f_name, 'r')

    while True:
        o_write = raw_input("Create new file (c) or overwrite existing (o): ")

        if o_write.lower() == 'o':
            print 'o'
            f_write = codecs.open(f_name, 'w')
            break
        elif o_write.lower() == 'c':
            print 'c'
            f_name_new = raw_input("What is new file name? ")
            f_write = codecs.open(f_name_new, 'w')
            break

