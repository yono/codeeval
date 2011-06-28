#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def fizzbuzz(input):
    fizz, buzz, limit = map(int, input.split(' '))

    result = []
    for i in xrange(1, limit + 1):
        output = i
        if (i % (fizz * buzz)) == 0:
            output = 'FB'
        elif (i % fizz) == 0:
            output = 'F'
        elif (i % buzz) == 0:
            output = 'B'
        result.append(output)

    return ' '.join(map(str, result))

infile = open(sys.argv[1]).read().splitlines()

for line in infile:
    print fizzbuzz(line)
