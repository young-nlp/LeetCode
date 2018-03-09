# coding:utf-8
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
 

Example:
Input: "cbbd"
Output: "bb"

Hint:
遍历每个字符，以该字符为中心向左右两边扩伸，直到该子串不是回文，返回的则是以该字符为中心最长回文子串。
以两个字符为中心同理。
'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sub = ""
        for i in range(0,len(s)):
            # 子串长度为奇数
            tmp = self.findsub(s,i,i)
            if len(tmp)>len(sub):
                sub = tmp
            # 子串长度为偶数
            tmp = self.findsub(s,i,i+1)
            if len(tmp)>len(sub):
                sub = tmp
        return sub
    def findsub(self,s,i,j):
        while(i>=0 and j<len(s) and s[i]==s[j]):
            i-=1
            j+=1
        return s[i+1:j]