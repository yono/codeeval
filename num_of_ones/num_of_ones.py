#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

infile = open(sys.argv[1]).read().splitlines()

TARGET_CHAR = '1'

for line in infile:
    char_count = 0
    binary = str(format(int(line), 'b'))

    for c in binary:
        if c == TARGET_CHAR:
            char_count = char_count + 1
    print char_count
