import os

def paths():
    """Print the full path to all files in the current directory, one per line"""

    print_files_title = u"Print Full Path of All Files in Current Directory"
    print print_files_title
    print u"-" * len(print_files_title)

    directory_list = os.listdir('.')
    for item in directory_list:
        print os.path.abspath(item)
    print u""


def file_copy():
    """Copies a file from a source to a destination (without using shutil or the OS copy command)"""

    copy_file_title = u"Copy a File"
    print copy_file_title
    print u"-" * len(copy_file_title)

    source_file = raw_input("Enter the name of an existing source file and press Enter: ")
    
    while source_file != None:
        try:
            f = open(source_file)
        except IOError:
            source_file = raw_input("Source file '%s' does not exist, try again: " % source_file)
        else:
            break

    destination_file = raw_input("Enter a destination file name and press Enter: ")

    # Open the destination file for writing, and write each line from the source file into the destination file
    outfile = open(destination_file, 'w')

    try:
        for line in f:
            outfile.write(line)
    except IOError as the_io_error:
        print the_io_error
    else:
        print u"File copy successful! Good bye."
        print u""

if __name__ == '__main__':
    print u""
    paths()
    file_copy()