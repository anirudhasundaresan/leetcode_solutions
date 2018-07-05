## Problem Statement ##
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2

Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?



## My Python3 code ## (Best answer: return int((1+len(nums))*len(nums)/2-sum(nums))) [sum of all nums - what should have been the sum] 
## same as: ((sum(range(len(nums)+1)) - sum(nums)))
class Solution: 
# (From SO) But the fact that it documents that dicts are hash tables implies pretty strongly that key in d, d[key], and d.get(key) are all going to be O(1).
    def missingNumber(self, nums):
        largest = max(nums)
        dic={}
        for i in nums:
            dic[i] = i
        for i in range(largest+2):
            if i not in dic:
                return i 
                
        ''' (TLE)
    def missingNumber(self, nums):
        largest = max(nums)
        for i in range(largest+2):
            if i not in nums:
                return i 
        '''
        """
        :type nums: List[int]
        :rtype: int
        """
        
