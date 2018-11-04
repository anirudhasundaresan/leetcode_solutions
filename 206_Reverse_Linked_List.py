#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

## My Python code ## (iterative)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        # This can be done in an iterative or recursive fashion 
        if head==None:
            return head
        prev_node = None
        next_node = head.next 
        while head is not None:
            head.next = prev_node
            prev_node = head
            head = next_node
            if not next_node==None:
                next_node = next_node.next              
        return prev_node

        """
        :type head: ListNode
        :rtype: ListNode
        """
        
