#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
Example 1:
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 
Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

## My Python3 code ##

import numpy as np
class Solution:
    def shortestToChar(self, S, C):
        arr = [1] * len(S)
        loc0 = []
        for index, char in enumerate(S):
            if S[index]== C:
                arr[index] = 0
                loc0.append(index)
        
        for i in range(len(arr)):
            if not i in loc0:
                final = []
                for j in range(len(loc0)):
                    final.append(abs(loc0[j] - i))
                arr[i] = min(final)
        return arr
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        
