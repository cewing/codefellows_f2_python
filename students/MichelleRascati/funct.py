import codecs


def funct(f_name):
    """Remove leading and trailing whitespace from file."""
    f_read = codecs.open(f_name, 'r')
    f_lines = f_read.readlines()
    out_lines = map(str.strip, f_lines)
    f_read.close()

    while True:
        o_write = raw_input("Create new file (c) or overwrite existing (o): ")

        if o_write.lower() == 'o':
            # f_name stays the same
            break
        elif o_write.lower() == 'c':
            f_name = raw_input("What is new file name? ")
            break

    f_write = codecs.open(f_name, 'w')

    for line in out_lines:
        f_write.write(line + '\n')
    print '"{}" has been written with no leading or trailing \
whitespace.'.format(f_name)


def funct_comp(f_name):
    """Remove leading and trailing whitespace from file w/ comprehension."""
    f_read = codecs.open(f_name, 'r')
    f_lines = f_read.readlines()
    print f_lines
    # out_lines = map(str.strip, f_lines)
    out_lines = [line.strip() for line in f_lines]
    print out_lines
    f_read.close()

    while True:
        o_write = raw_input("Create new file (c) or overwrite existing (o): ")

        if o_write.lower() == 'o':
            # f_name stays the same
            break
        elif o_write.lower() == 'c':
            f_name = raw_input("What is new file name? ")
            break

    f_write = codecs.open(f_name, 'w')

    for line in out_lines:
        f_write.write(line + '\n')
    print '"{}" has been written with no leading or trailing \
whitespace.'.format(f_name)
