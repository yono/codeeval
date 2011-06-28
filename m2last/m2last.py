#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

infile = open(sys.argv[1]).read().splitlines()

for line in infile:
    if line == '':
        continue
    data = line.split(' ')
    num = int(data.pop(-1))
    if num > len(data):
        continue
    print data[num * -1]
