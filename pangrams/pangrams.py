#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

infile = open(sys.argv[1]).read().splitlines()

alphabets = set('abcdefghijklmnopqrstkvwxyz')

for line in infile:
    if len(line) == 0:
        continue
    char_set = set([])
    for c in line:
        char = c.lower()
        if char in alphabets:
            char_set.update(char)
    missing_chars = alphabets.difference(char_set)
    if len(missing_chars) == 0:
        print 'NULL'
    else:
        missing_list = list(missing_chars)
        missing_list.sort()
        print ''.join(missing_list)
