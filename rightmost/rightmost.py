#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

infile = open(sys.argv[1]).read().splitlines()

for line in infile:
    if line == '':
        continue

    string, char = line.split(',')
    index = -1
    for i,s in enumerate(string):
        if char == s:
            index = i 
    print index
