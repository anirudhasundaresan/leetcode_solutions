#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
Given a linked list, remove the n-th node from the end of list and return its head.
Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Follow up:
Could you do this in one pass?

## My Python code ##
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        # Use two pointer method.
        if head==None or head.next==None:
            return None
        v_pointer, v2_pointer = head, head
        while n!=0:
            v2_pointer = v2_pointer.next
            n = n-1
        if v2_pointer!=None:
            while v2_pointer.next!=None:
                v2_pointer=v2_pointer.next
                v_pointer=v_pointer.next
            if v_pointer.next!=None:
                v_pointer.next = v_pointer.next.next
        else:
            return v_pointer.next
        return head
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
