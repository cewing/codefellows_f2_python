import os
import codecs


def p_path():
    """Print full path to all files in current directory."""
    cwd = os.getcwdu()
    files = os.listdir(cwd)
    for f in files:
        print cwd + '/' + f


def copy_file(source, dest):
    """Copy a file from source to dest[ination] folder."""
    f_name = os.path.relpath(source)
    f_dest = dest + '/' + f_name

    infile = codecs.open(source, 'r')
    lines = infile.readlines()
    outfile = codecs.open(f_dest, 'w')
    for line in lines:
        outfile.write(line)
    infile.close()
    outfile.close()
