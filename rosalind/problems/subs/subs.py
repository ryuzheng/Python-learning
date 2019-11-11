# -*- coding: utf-8 -*-
'''
/*
 * @Author: Zexin Zheng
 * @Date: 2019-11-11 17:29:59
 * @Last Modified by: Zexin Zheng
 * @Last Modified time: 2019-11-11 17:36:02
 */
'''

with open('rosalind_subs.txt', 'r') as f1:
    string = f1.readline().strip()
    substring = f1.readline().strip()
    # print(string, substring)

print(' '.join([str(i + 1) for i in range(len(string)) if string.startswith(substring, i)]))
