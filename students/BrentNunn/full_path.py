#!/usr/bin/env python

import os

directory = os.getcwdu()
files = os.listdir(directory)

for f in files:
    print os.path.join(directory, f)

