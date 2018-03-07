#coding:utf-8
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Hint:
一开始的思路是从最长子串遍历，如果有不重复字符即返回。但这样做的时间复杂度太高了。
对比其他人的思路，用了字典来存储每个不重复字符的最近索引，并用start记录当前不重复子串的起始位置，
如果遇到重复字符，即把start往后移一位，继续遍历，如此时间复杂度只有O(N)。
'''

class Solution:
    def mylengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slen = len(s)
        for sublen in range(slen,0,-1):
            for i in range(0,slen-sublen+1):
                print(s[i:i+sublen])
                if len(set(s[i:i+sublen])) == sublen:
                    return sublen
        return 0

    def lengthOfLongestSubstring(self, s):    
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        
        return max_length

