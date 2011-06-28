#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

infile = open(sys.argv[1]).read().splitlines()

for line in infile:
    list1_str, list2_str = line.split(';')
    list1 = list1_str.split(',')
    list2 = list2_str.split(',')

    list1_set = set(list1)
    list1_set.intersection_update(set(list2))
    result_list = list(list1_set)
    result_list.sort()
    print ','.join(result_list)
