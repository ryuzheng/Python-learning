# -*- coding: utf-8 -*-
'''
/*
 * @Author: Zexin Zheng
 * @Date: 2019-11-07 17:27:37
 * @Last Modified by: Zexin Zheng
 * @Last Modified time: 2019-11-07 19:05:29
 */
'''

import sys

# k, m, n = 2, 2, 2

with open(sys.argv[1], 'r') as fi:
    line = fi.read().strip()
    k, m, n = line.split(' ')

k = int(k)
m = int(m)
n = int(n)

total = sum([k, m, n])

aa1 = 0.25 * m / total * (m - 1) / (total - 1)
aa2 = 0.5 * m / total * n / (total - 1) + 0.5 * n / total * m / (total - 1)
aa3 = n / total * (n - 1) / (total - 1)

print(1 - aa1 - aa2 - aa3)
