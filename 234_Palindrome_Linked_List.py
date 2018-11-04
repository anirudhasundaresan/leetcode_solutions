## Problem Statement ##
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

## My Python3 code ##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## Two methods to do this: 
## Using a stack; go through the list and append the stack with the elements. Compare the popped elements of the stack with the LL elements upon normal traversal again. Time: O(n+n); Space: O(n)--due to stack 
## Better solution: Go through the list and find length -- Reverse 2nd half of the LL and compare element wise with first half. 
## Even better solution: Use 2 pointer to reverse the 2nd half, O(N) now, and then continue as before. 

class Solution:
    def isPalindrome(self, head):
        v_pointer = head
        v2_pointer = head
        if head==None:
            return True
        if head.next==None:
            return True
        
        while v2_pointer!=None:
            if v2_pointer.next!=None: 
                v_pointer = v_pointer.next
                v2_pointer = v2_pointer.next.next 
            else:
                break
        next_node = v_pointer.next
        prev_node = None
        while v_pointer!=None:
            v_pointer.next = prev_node
            prev_node = v_pointer
            v_pointer = next_node
            if next_node!=None:
                next_node = next_node.next
        while prev_node!=None:
            if head.val == prev_node.val:
                head = head.next
                prev_node = prev_node.next
                continue
            else:
                return False
        return True


        """
        :type head: ListNode
        :rtype: bool
        """
        
