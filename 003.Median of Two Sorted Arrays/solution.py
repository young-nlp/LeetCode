# coding:utf-8
'''
Description:
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

Hint:
把寻找两个排好序数组的中位数转化成找第k大数，由于要求时间复杂度为O(log(m+n))，自然而然想到二分法进行递归。
首先判断中位数如果是在两个数组的后半部分，则比较两个数组中位数大小，较小的数组前半部分直接扔掉（因为中位数
肯定不存在于这里）只留下后半部分与较大数组进行递归计算，第k大个数也要相应减小扔掉的数组元素个数。
中位数如果在两个数组的前半部分，则比较两个数组中位数大小，较大的数组后半部分扔掉（因为中位数肯定不存在于这里）
再把前半部分与较小的数组进行递归计算，由于扔掉的是比第k个数大的数组元素，所以继续求第k大数。
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if (m+n)%2 == 1:
            return self.kthOfTwoArrays(nums1,nums2,(m+n)//2)
        else:
            return (self.kthOfTwoArrays(nums1,nums2,(m+n)//2-1)+self.kthOfTwoArrays(nums1,nums2,(m+n)//2))/2
    
    def kthOfTwoArrays(self,nums1,nums2,k):
        print(nums1,nums2,k)
        if len(nums1) == 0:
            return nums2[k]
        if len(nums2) == 0:
            return nums1[k]
        
        p1, p2 = len(nums1)//2, len(nums2)//2
        v1, v2 = nums1[p1], nums2[p2]

        if k > p1+p2:
            if v1 > v2:
                return self.kthOfTwoArrays(nums1,nums2[p2+1:],k-p2-1)
            else:
                return self.kthOfTwoArrays(nums1[p1+1:],nums2,k-p1-1)
        else:
            if v1 > v2:
                return self.kthOfTwoArrays(nums1[:p1],nums2,k)
            else:
                return self.kthOfTwoArrays(nums1,nums2[:p2],k)
        
if __name__ == "__main__":
    s = Solution()
    a = [1,2]
    b = [3,4]
    result = s.findMedianSortedArrays(a,b)
    print(result)