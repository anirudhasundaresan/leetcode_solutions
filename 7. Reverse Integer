## Problem Statement ##
Given a 32-bit signed integer, reverse digits of an integer.
Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## My Python3 code ##

import math 
class Solution:
    def reverse(self, x):
        if abs(x) >= math.pow(2,31):
            return 0
        x = str(x) 
        if x[0] == '-':
            y = x[1:len(x)] 
            if abs(int(y[::-1])) >= math.pow(2,31):
                return 0
            else:
                return(-int(y[::-1]))
            
        if x[len(x)-1]==0:
            return(int(x[::-2]))
            
        if abs(int(x[::-1])) >= math.pow(2,31):
            return 0
        else: 
            return(int(x[::-1]))
        
