#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

## My Python code ##
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        indexA = 0
        indexB = 0
        pointerA = headA
        pointerB = headB
        if headA == None or headB == None:
            return None
        while pointerA!= None:
            indexA = indexA + 1
            pointerA = pointerA.next
        while pointerB!= None:
            indexB = indexB + 1
            pointerB = pointerB.next
        poA = headA
        poB = headB
        diff = abs(indexA - indexB)

        if indexA >= indexB: #traverse diff nodes in A and then start comparing.
            while diff!=0:
                poA = poA.next
                diff = diff - 1
            while poA.next!=None:
                if poA==poB:
                    return poA
                poA = poA.next
                poB = poB.next
            if poA==poB:
                return poA
            return None

        if indexA < indexB:
            while diff!=0:
                poB = poB.next
                diff = diff - 1
            while poB.next!=None:
                if poB==poA:
                    return poB
                poB = poB.next
                poA = poA.next
            if poA == poB:
                return poA
            return None
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

## Better solution: ##

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        trav_a, trav_b = headA, headB
        while trav_a is not trav_b:
            trav_a = headB if not trav_a else trav_a.next
            trav_b = headA if not trav_b else trav_b.next
        return trav_a
