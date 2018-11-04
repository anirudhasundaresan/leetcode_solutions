#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

## My python3 code ##
## Trick is identifying that this is the Fibonacci sequence. 6 methods in Leetcode solutions. 
'''
- Fibo normal recursion: O(n) time + O(1) space
- Fibo formula: O(log n) time + O(1) space
- DP: O(n) time + O(n) space
- Binets method: O(log n) time + O(1) space
'''
from math import sqrt ## takes up O(log n)
class Solution(object):
    def climbStairs(self, n):
        return int(((1+sqrt(5))**(n+1)-(1-sqrt(5))**(n+1))/(2**(n+1)*sqrt(5)))
        """
        :type n: int
        :rtype: int
        """
        
