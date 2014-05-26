#fullpath.py

import os

def file_list():
    '''prints the full path to all files in the 
        current directory, one per line '''
    path = os.getcwd()
    dirs = os.listdir( path )

    for file in dirs:
        print path + '/' + file

file_list()