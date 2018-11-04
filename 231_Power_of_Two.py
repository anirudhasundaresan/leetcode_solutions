## Problem Statement ##
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Example 2:

Input: 16
Output: true
Example 3:

Input: 218
Output: false

## My Python3 code ## (better:  return True if n & (n-1) == 0 and n != 0 else False)
class Solution:
    def isPowerOfTwo(self, n):
        if n<0:
            return False            ## forgot this initially
        if bin(n)[2:].count('1')==1:
            return True
        return False
        """
        :type n: int
        :rtype: bool
        """
