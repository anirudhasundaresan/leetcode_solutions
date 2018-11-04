#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##
Given a linked list, determine if it has a cycle in it.
Follow up:
Can you solve it without using extra space?

## My Python code ##

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution(object): 
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        v_pointer = head 
        v2_pointer = head
        while v2_pointer!=None:
            if v2_pointer.next == None:
                v2_pointer = v2_pointer.next
            else:
                v2_pointer = v2_pointer.next.next
            v_pointer = v_pointer.next
            if v_pointer == v2_pointer:
                return True
        return False
            
        """
        :type head: ListNode
        :rtype: bool
        """
        

## Better solution ##

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        node, prev = head, None
        while node:
            if node.next==False:
                return True            
            node, prev = node.next, node
            prev.next = False

        return False
