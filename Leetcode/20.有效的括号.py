#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.70%)
# Total Accepted:    52.1K
# Total Submissions: 141.7K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#
class Solution:
    def isValid(self, s: str) -> bool:
        # NOTE: python 栈
        lefts = {"[", "{", "("}
        rights = {"]", '}', ")"}
        stack = []
        for x in s:
            if x in lefts:
                stack.append(x)
            elif x in rights:
                if not stack or not (1 <= ord(x) - ord(stack[-1]) <= 2):
                    return False
                stack.pop()
        return not stack
