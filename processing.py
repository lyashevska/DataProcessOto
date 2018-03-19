#!/usr/bin/env python3

import re
import os
from glob import glob
import csv

# change dir
dirname = os.path.dirname(__file__)
datadir = os.path.join(dirname,'data')
os.chdir(datadir)

filenames = glob('*.txt')

results = []
for i in range(len(filenames)):
    f = open(filenames[i], 'r')
    lines = f.readlines()
    #f.close()
    res = []
    for line in lines:
        # line containing tif
        m1 = re.search("^.*tif.*$", line)
        if m1:
            #print(m1.group)
            fishid = m1.group().split(".tif")[0]

        # line starting with numeric
        m2 = re.search("^\d.*", line)
        if m2:
            #print(m2.group())
            z = fishid + '\t' + m2.group()
            print(z)
            res += [z]
    results+=res

# write to a file
with open("../output.csv", "w") as f:
    for item in results:
        f.write(item)
        f.write("\n")

