#coding:utf-8
'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Hint:
输入是两个反序的链表，要求对两个链表求和之后输出和的反序链表。
即把加法从左往右计算即可，注意进位和链表是否为空的判断。

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lastadd = 0
        temp = result = ListNode(0)
        while True:
            cursum = lastadd
            if l1:
                cursum +=l1.val
                l1 = l1.next
            if l2:
                cursum +=l2.val
                l2 = l2.next
            lastadd = cursum // 10
            curval = cursum % 10
            temp.next = ListNode(curval)
            temp = temp.next
            if (l1 == None) and (l2 == None) and (lastadd==0):
                break
        
        return result.next
            
            
            