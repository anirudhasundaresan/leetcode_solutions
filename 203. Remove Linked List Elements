## Problem Statement ##
Remove all elements from a linked list of integers that have value val.
Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

## My Python3 code ##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        current_node = head
        prev_node = ListNode(0)
        prev_node.next = head
        while current_node!=None:
            if current_node.val==val:
                if prev_node.next==head:
                    head = head.next
                    prev_node.next = head
                else:
                    prev_node.next = current_node.next
            else:
                prev_node = prev_node.next
            current_node = current_node.next
        return head
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
