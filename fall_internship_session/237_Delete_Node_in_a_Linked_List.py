#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

## My Python code ##
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):

        # Since node value is given, we need not iterate through the entire list. If only node index is given, we need to iterate...
        # Note: Here, in Q definition, no def of linked list. That means, they want us to find a solution better than iterating through the LL.
        # 0(N) --- Start with given node..iterate till end...shift one by one to the left and make last one 0.
        # O(1) --- Shift 4 to 3, and make new 4 point to 5. --- Best solution.
        # Code for O(1):
        # No need to create a new nextnode...do everything inplace. But readability will take a hit!
        node.val = node.next.val
        node.next = node.next.next
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

