#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

endians = {'little': 'LittleEndian', 'big': 'BigEndian'}

print endians[sys.byteorder]
