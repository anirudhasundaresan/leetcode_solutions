#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

## My Python3 code ##
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        
        if l1.val <= l2.val:
            head = l1
            temp2 = l2
        else:
            head = l2
            temp2 = l1
        temp1 = head.next
        main_node = head
        
        while temp1!=None and temp2!=None:
            if temp2.val <= temp1.val:
                head.next = temp2
                head = head.next
                temp2 = temp2.next
            else:
                head.next = temp1
                head = head.next
                temp1 = temp1.next  
                
        while temp1!=None and temp2==None:
            head.next = temp1
            head = head.next
            temp1 = temp1.next
        while temp2!=None and temp1==None:
            head.next = temp2
            head = head.next
            temp2 = temp2.next
                
        head.next = None
        return main_node
            
            
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
