#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def get_smallest_multiple(threshold, num):
    i = 1
    while 1:
        if threshold <= (num * i):
            return (num * i)
        else:
            i += 1

infile = open(sys.argv[1]).read().splitlines()

for line in infile:
    threshold, num = map(int,line.split(','))

    print get_smallest_multiple(threshold, num)
