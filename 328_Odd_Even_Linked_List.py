## Problem Statement ##
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
Example:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

## My Python3 code ##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        odd_node = head
        if head==None:
            return head
        elif head.next==None:
            return head
        even_node = head.next
        temp = head.next
        while True:
            if even_node.next==None:
                odd_node.next = temp
                return head
            odd_node.next = even_node.next 
            odd_node = even_node.next
            if odd_node.next==None: 
                odd_node.next = temp
                even_node.next = None
                return head
            even_node.next = odd_node.next
            even_node = odd_node.next  
       
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
