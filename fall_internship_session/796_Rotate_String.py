#!/home/anirudha/anaconda3/bin/python

## Problem Statement ##

'''
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
'''

## My Python3 code ##

class Solution:
    def rotateString(self, A, B):
        if A=='' and B=='':
            return True
        for i in range(len(A)):
            if B == (A[1:] + A[0]):
                return True
            A = A[1:] + A[0]
        return False
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
'''
# Better code:

from collections import Counter
class Solution(object):
    def rotateString(self, A, B):
        if not len(A)==len(B):
            return False
        if not Counter(B) - Counter(A)==Counter():
            return False
        A = A + A
        if B in A:
            return True
        else:
            return False

        """
        :type A: str
        :type B: str
        :rtype: bool
        """
'''

