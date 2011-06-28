#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def fib(n):
    if n > 1:
        return fib(n - 1) +  fib(n -2)
    else:
        return n

infile = open(sys.argv[1]).read().splitlines()

for line in infile:
    print fib(int(line))
