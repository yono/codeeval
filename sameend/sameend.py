#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

infile = open(sys.argv[1]).read().splitlines()

for line in infile:
    if line == '':
        continue
    main, sub = line.split(',')
    if (main.find(sub) + len(sub)) == len(main):
        print '1'
    else:
        print '0'
