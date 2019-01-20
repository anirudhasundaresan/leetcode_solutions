#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5



## My Python code ##
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    ### Answer is simpler if I use ListNode() objects and then appended them with each part. 
    def partition(self, head, x):
        h = ListNode(0)
        l = ListNode(0)
        g = h
        y = l
        current_node = head
        while current_node!=None:
            if current_node.val >= x:
                h.next = current_node
                h = h.next
            else:
                l.next = current_node
                l = l.next
            current_node = current_node.next
        l.next = g.next
        h.next = None
        return y.next
        


        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
