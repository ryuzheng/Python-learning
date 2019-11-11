# -*- coding: utf-8 -*-
'''
/*
 * @Author: Zexin Zheng
 * @Date: 2019-11-11 18:47:55
 * @Last Modified by: Zexin Zheng
 * @Last Modified time: 2019-11-11 18:57:25
 */
'''

import sys

# NOTE:
'''
parents      expect value
1. AA-AA        1
2. AA - Aa      1
3. AA - aa      1
4. Aa - Aa      3/4
5. Aa - aa      1/2
6. aa - aa      0
||
||
    |  A       a
-----------------
A   | AA      Aa
a   | Aa      aa 
'''


def cal_expect(args):
    parent_1, parent_2, parent_3, parent_4, parent_5, parent_6 = args
    expect_1 = int(parent_1)
    expect_2 = int(parent_2)
    expect_3 = int(parent_3)
    expect_4 = int(parent_4) * 3 / 4
    expect_5 = int(parent_5) * 1 / 2
    expect_6 = 0
    return sum([expect_1, expect_2, expect_3, expect_4, expect_5]) * 2


with open(sys.argv[1], 'r') as f1:
    argvs = f1.readline().strip().split(' ')

print(cal_expect(argvs))
