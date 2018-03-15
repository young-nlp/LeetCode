# coding:utf-8
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Hint:
这道题目初看和2Sum的题目有点像，但由于是3个数相加和为0，解法上还是有所区别。
首先对数组进行排序，遍历时首先确定最小数，再从大于该数的右部分数组左右同时遍历，找到三者和为0的组合。
由于要求返回结果不能重复，所以注意对于重复的元素要跳过，否则会造成重复统计。
'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nLen = len(nums) 
        nums.sort()
        for i in range(0, nLen):
            if i>0 and nums[i]==nums[i-1]:
                continue
            s = -nums[i]
            l, r = i+1, nLen-1
            while(l<r):
                if nums[l]+nums[r] == s:
                    results.append([nums[i],nums[l],nums[r]])
                    while(l<r and nums[l]==nums[l+1]):
                        l += 1
                    while(l<r and nums[r]==nums[r-1]):
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l]+nums[r]<s:
                    l += 1
                else:
                    r -= 1
        return results
                    
