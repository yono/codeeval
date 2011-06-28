#!/usr/bin/env python
# -*- coding:utf-8 -*-

def is_palindrome(num):
    str_num = str(num)
    is_odd = (num % 2) == 1
    is_palindrome = False

    for i in xrange(0, len(str_num)/2):
        if str_num[i] != str_num[len(str_num) - i - 1]:
            return False
        
    return True

maxnum = 1000
prime_nums = []
for i in xrange(2, maxnum + 1):
    for j in prime_nums:
        if (i % j) == 0:
            break
    else:
        prime_nums.insert(0, i)

for i in prime_nums:
    if is_palindrome(i):
        print i
        break
