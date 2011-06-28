#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def len_sort(x, y):
    return len(y) - len(x)

infile = open(sys.argv[1]).read().splitlines()
num = int(infile.pop(0))
lines = []
for line in infile:
    if len(lines) < num:
        lines.append(line)
    elif len(lines[-1]) < len(line):
        lines.pop(-1)
        lines.append(line)
    lines.sort(len_sort)

for line in lines:
    print line
