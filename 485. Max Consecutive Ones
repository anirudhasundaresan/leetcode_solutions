## Problem Statement ##
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000

## My Python3 code ##
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        nums.append(0)
        if nums.count(1)==0:
            return 0
        ct, ctr=0,0
        for i in range(len(nums)):
            if nums[i]==1 and nums[i+1]==1:
                ct+=1
            else:
                ctr = max(ct, ctr)
                ct=0
        return ctr+1
        """
        :type nums: List[int]
        :rtype: int
        """
        
