#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import re

infile = open(sys.argv[1]).read().splitlines()

for line in infile:
    string, chars = line.split(',')
    chars = chars.replace(' ', '')
    regex = re.compile(r'[%s]' % (chars))

    print regex.sub('', string)
