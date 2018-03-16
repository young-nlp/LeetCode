# coding:utf-8
'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

Hint:
思路1：利用一个数组存储每个链表结点的地址，直接利用索引删掉倒数第n个结点
思路2：利用了两个指针，一个是快指针，一个是慢指针，首先快指针遍历到第n+1个结点，
此时与慢指针相隔n个结点，然后两者同时继续往后遍历，直到快指针达到最后一个结点。
此时慢指针所指的结点就是要删掉的结点的上一结点，直接删除。
（注意边界）

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmpNode = []
        dummy = head
        while(dummy!=None):
            tmpNode.append(dummy)
            dummy = dummy.next
        if n == len(tmpNode):
            if n == 1:
                head = None
            else:
                head = tmpNode[1]
        else:
            tmpNode[-(n+1)].next = tmpNode[-n].next
        return head
        
class OtherSolution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
