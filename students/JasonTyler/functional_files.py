#!/usr/bin/env python
"""Functional Files assignment"""
from sys import argv
import os


IOERR_MESSAGE = "Can't find/read file. Check path and permissions."


def doc_strip(source_file, overwrite=False):
    """Strips leading/trailing whitespace from file lines"""
    # Read file before any writing
    line_list = get_source_lines(source_file)
    # Assign file variables based on mode
    if overwrite:
        try:
            out_file = open(source_file, 'w+')
        except IOError:
            print IOERR_MESSAGE
    else:
        try:
            out_file = open(append_new(source_file), 'w+')
        except IOError:
            print IOERR_MESSAGE
    #source_text = in_file.read() 
    #out_file.writelines(line_list)
    for n in range(len(line_list)):
        # if/else to prevent appending additional line to file
        if n != len(line_list) - 1:
            out_file.write(line_list[n].strip()+'\n')
        else:
            out_file.write(line_list[n].strip())
    # Cleanup
    out_file.close()
    del line_list


def append_new(filename):
    """Append _new to file name, such that file.ext becomes file_new.ext"""
    new_file_name = list(os.path.splitext(filename))
    new_file_name.insert(1, '_new')
    return "".join(new_file_name)


def get_source_lines(filename):
    """Return source text to list of lines"""
    try:
        with open(filename) as file:
            source_text = file.read()
            source_text = source_text.split('\n')
    except IOError:
        print IOERR_MESSAGE
    else:
        return source_text


if __name__ == "__main__":
    if 1 < len(argv) <= 3:
        try:
            overwrite_flag = bool(argv[2])
        except IndexError:
            # If no overwrite flag is present, try calling doc_strip with default behavior
            if os.path.exists(argv[1]):
                doc_strip(argv[1])
            else:
                print IOERR_MESSAGE
        else:
            # Nested if/else to check for that source file exists
            if os.path.exists(argv[1]):
                doc_strip(argv[1], overwrite_flag)
            else:
                print IOERR_MESSAGE
    else:
        print """
        Usage:

            functional_files.py filename [True/False]

        where [True/False] indicates overwrite permissions
        (defaults to False).
        """
