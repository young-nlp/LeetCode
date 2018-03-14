'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = x<0
        m = abs(x)
        n = 0
        s = 0
                    
        while(m!=0):
            d = m%10
            s = s*10+d
            m = m//10
        
        if rev:
            s = 0-s
        if s < -2**31 or s > 2**31-1:
            s = 0 
        return s
            
