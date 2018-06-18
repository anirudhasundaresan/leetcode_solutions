## Problem Statement ##
 Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

## My Python3 code ##
class Solution:
    def isPowerOfFour(self, num): ## all three approaches place me in the same percentile
        # this is the actual bit manipulation technique, not my own 
        if num <= 0:
            return False
        # any power of 4 and it's one smaller will follow first condition
        return num & (num-1) == 0 and num & 0xAAAAAAAA == 0     # second condition for even numbers not a power of 4 
        '''
        arr = list(bin(num)[2:])
        if arr.count('1')==1: # using loops again in CPython code :/.I think they want bit manipulation
            if arr.index('1')==0 and len(arr)%2!=0:
                return True
            else:
                return False
        else:
            return False
        '''
        '''
        if num==1 or num==4:
            return True
        while num!=4:
            if bin(num)[-2:]=='00':
                num=num>>2
                if num==4:
                    return True
            else:
                return False
        '''
        """
        :type num: int
        :rtype: bool
        """
        
