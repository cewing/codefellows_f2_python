import os


def print_path(path=os.getcwd()):
    u"""Print all files in a given path."""
    files = os.listdir(path)
    for file_ in files:
        print file_