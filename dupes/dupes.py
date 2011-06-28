#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

infile = open(sys.argv[1]).read().splitlines()

for line in infile:
    sorted_list = line.split(',')
    result_list = []
    for num in sorted_list:
        if len(result_list) == 0:
            result_list.append(num)
        elif result_list[-1] != num:
            result_list.append(num)
    print ','.join(result_list)
