import os
from os import listdir
from os.path import isfile, join

cwd = os.getcwd()
onlyfiles = [ f for f in listdir(cwd) if isfile(join(cwd,f)) ]
for a_file in onlyfiles:
    print os.path.dirname(os.path.realpath(a_file)) + "/%s"%a_file