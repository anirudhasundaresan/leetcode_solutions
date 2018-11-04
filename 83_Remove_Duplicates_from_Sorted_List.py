#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''


Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

## My Python3 code ##
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        prev_node = None
        current_node = head
        while current_node!=None:
            if prev_node!=None:
                if current_node.val == prev_node.val:
                    prev_node.next = current_node.next
                else:
                    prev_node = current_node
            else:
                prev_node = current_node
            current_node = current_node.next
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
