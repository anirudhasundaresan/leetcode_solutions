## Problem Statement ##
 Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:

Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.

Note:

    N is a positive integer and won't exceed 10,000.
    All the scores of athletes are guaranteed to be unique.


## My Python3 code ##
class Solution:
    def findRelativeRanks(self, nums):
        nums_s = sorted(nums, reverse=True)
        if len(nums)==2:
            nums[nums.index(nums_s[0])] = 'Gold Medal'
            nums[nums.index(nums_s[1])] = 'Silver Medal'
        elif len(nums)==1:
            nums[nums.index(nums_s[0])] = 'Gold Medal'
        else:
            nums[nums.index(nums_s[0])] = 'Gold Medal'
            nums[nums.index(nums_s[1])] = 'Silver Medal'
            nums[nums.index(nums_s[2])] = 'Bronze Medal'
        j=4
        for i in range(3, len(nums)):
            nums[nums.index(nums_s[i])] = str(j) 
            j+=1
        return nums
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
