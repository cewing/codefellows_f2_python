import os, sys

def copy_to(in_file, out_file):
    '''copies a file from a source, to a destination 
    (provide path and name for out_file) '''
    f = open(in_file, 'r+')
    contents = f.read()
    outfile = f.write(contents)

copy_to("copy_files.txt", "copied.txt")

"""
What to do:
open file
read file
write file to new name at new path.
"""

# Job:write a program which copies a file from a source, to a destination 
# (without using shutil, or the OS copy command)