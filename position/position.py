#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

infile = open(sys.argv[1]).read().splitlines()

for line in infile:
    num, p1, p2 = map(int, line.split(','))
    num_bit = str(format(num, 'b'))

    if num_bit[len(num_bit)-p1] == num_bit[len(num_bit)-p2]:
        print 'true'
    else:
        print 'false'
