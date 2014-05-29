import os, sys

def copy_to(in_file, out_file):
    '''copies a file from a source, to a destination 
    (provide path and name for out_file) '''
    f = open(in_file, 'rb')
    out = open(out_file, 'wb')
    contents = f.read()
    outfile = out.write(contents)

copy_to("copy_files.txt", "copied.txt")

