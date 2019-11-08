# -*- coding: utf-8 -*-
'''
/*
 * @Author: Zexin Zheng
 * @Date: 2019-11-08 17:57:24
 * @Last Modified by: Zexin Zheng
 * @Last Modified time: 2019-11-08 18:12:39
 */
'''

import sys

with open(sys.argv[1]) as fi:
    content = fi.read().strip()
    n, k = content.split(' ')
    n = int(n)
    k = int(k)

# NOTE: Fn=Fn-1+Fn-2*k, range(1,n+1)
# n = 5
# k = 3

Fn_1 = 1
Fn_2 = 0
m = 0
for month in range(2, n+1):
    Fn = Fn_1 + m * Fn_2
    Fn_2 = Fn_1
    Fn_1 = Fn

    # print(Fn, Fn_1, Fn_2)
    m = k

print(Fn)