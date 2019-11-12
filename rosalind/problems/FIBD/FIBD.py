# -*- coding: utf-8 -*-
'''
/*
 * @Author: Zexin Zheng
 * @Date: 2019-11-12 15:34:04
 * @Last Modified by: Zexin Zheng
 * @Last Modified time: 2019-11-12 18:02:00
 */
'''

import sys

with open(sys.argv[1]) as fi:
    content = fi.read().strip()
    n, k = content.split(' ')
    n = int(n)
    k = int(k)

# n = 9
# k = 4

# NOTE: 0、1、2、3.。个月的兔子，0代表本月出生的兔子
rabbits_of_month = [0] * (k + 1)
rabbits_of_month[0] = 1
# print(rabbits_of_month)

for month in range(2, n + 1):
    # NOTE: 往右推移，将到寿命的兔子推出
    rabbits_of_month[1:] = rabbits_of_month[:-1]
    # NOTE: 本月出生的兔子等于满2月的兔子所生
    rabbits_of_month[0] = sum(rabbits_of_month[2:])
    # print(rabbits_of_month)

print(sum(rabbits_of_month[:-1]))
