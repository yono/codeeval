#!/usr/bin/env python
# -*- coding:utf-8 -*-

maxnum = 1000
prime_nums = []
i = 1
cont = True
while 1:
    if len(prime_nums) == maxnum:
        cont = False
    if not cont:
        break
    i += 1
#for i in xrange(2, maxnum + 1):
    for j in prime_nums:
        if (i % j) == 0:
            break
    else:
        prime_nums.insert(0, i)

print sum(prime_nums)
