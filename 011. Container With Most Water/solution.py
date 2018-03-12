# coding: utf-8
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Hint:
要使容器体积最大，两个要素是水平距离和垂直高度，首先从左右两边开始遍历，分别用l和r代表横坐标，如果h[l]小于h[r]，此时以l为基准的容器体积达到最大，
执行l+1；如果此时h[r]小于h[l]，此时以r为基准的容器体积达到最大，执行r-1；每步都取当前体积最大的容器体积，遍历结束则得到结果。
'''

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        Max = 0
        l, r = 0, len(height)-1
        while(l!=r):
            if height[l]>height[r]:
                area = height[r]*(r-l)
                r-=1
            else:
                area = height[l]*(r-l)
                l+=1
            Max = max(Max,area)
        return Max
