## Problem Statement ##

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

## My Python3 code ##

class Solution(object):
    def moveZeroes(self, nums):
        lis = [1 for i in nums if i==0]
        for i in range(sum(lis)):
            nums.remove(0)
            nums.append(0) # it removes 0 from the start of the list...so this is fine 
            
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
