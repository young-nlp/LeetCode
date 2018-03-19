# coding: utf-8
'''
Determine whether an integer is a palindrome. Do this without extra space.

Hint: 可参考数字反转那道题，反转之后值相等即为互文。
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
       
        m = x
        s = 0
        
        while(m!=0):
            d = m%10
            s = s*10+d
            m = m//10
        return s==x
        
