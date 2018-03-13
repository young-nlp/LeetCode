# coding: utf-8
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {')':'(', '}':'{', ']':'['}
        stack = []
        for e in s:
            if stack and (e in map and stack[-1] == map[e]):
                stack.pop()
            else:
                stack.append(e)
        return not stack
