#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

infile = open(sys.argv[1]).read().splitlines()

for line in infile:
    print line.lower()
