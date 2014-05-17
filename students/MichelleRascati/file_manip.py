import os


def p_path():
    """Print full path to all files in current directory"""
    cwd = os.getcwdu()
    files = os.listdir(cwd)
    for f in files:
        print cwd + '/' + f
