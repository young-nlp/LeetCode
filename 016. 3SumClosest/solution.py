# coding:utf-8
'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        SUM = 0
        nums = sorted(nums)
        if len(nums) == 3:
            return sum(nums)
        MIN = abs(nums[0]+nums[1]+nums[2]-target)
        for i in range(0,len(nums)-2):
            l = i+1
            r = len(nums)-1
            while(l<r):
                s = nums[i]+nums[l]+nums[r]
                if s == target:
                    return s
                if abs(s-target) <= MIN:
                    SUM = s
                    MIN = abs(s-target)
                if s < target:
                    l+=1
                else:
                    r-=1
        return SUM
                
