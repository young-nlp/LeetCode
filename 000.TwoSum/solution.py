#coding:utf-8
'''
https://leetcode.com/problems/two-sum/description/

Description:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Hint:
题目要找到配对的两个数，使得其和等于target，最直接方法是遍历，但时间复杂度是n^2。
利用Key-Value数据结构，遍历时把a的值作为key，索引作为value存储在字典里，并找b的索引值。
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,a in enumerate(nums):
            b = target - a
            if b in d:
                return [d[b],i]
            else:
                d[a] = i
    