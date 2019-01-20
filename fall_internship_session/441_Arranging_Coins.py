#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

## My Python3 code ## (return int((math.sqrt(8*n + 1)-1)/2 )) -- fastest? : Running sum: 1+2+3+...x < n, find x. 
'''
class Solution:
    def arrangeCoins(self, n):
        if n==1 or n==0:
            return n
        nums=0
        j=-1
        for i in range(n+1): # ideally, only till n/2; use binary search
            nums+=i
            if nums>n:
                return j
            j+=1
                
        """
        :type n: int
        :rtype: int
        """
        
