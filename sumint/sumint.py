#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

print sum(map(int, open(sys.argv[1]).read().splitlines()))
