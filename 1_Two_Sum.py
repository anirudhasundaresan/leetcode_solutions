## Problem Statement ##

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

## My Python3 code ##

class Solution:
    def twoSum(self, nums, target):
        q = (len(nums))
        list = [(i,j) for i in range(q) for j in range(i+1,q) if target==nums[i]+nums[j]]
        return list[0]

