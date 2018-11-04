#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

## My Python3 code ##
'''

class Solution:
    def rotate(self, nums, k):
        rot = len(nums)-k
        if k!=0:
            if rot>=0:
                for i in range(rot):
                    nums.append(nums[0])
                    del nums[0]
            else:
                for i in range(k):
                    temp = nums[-1]
                    del nums[-1]
                    nums.insert(0,temp)  #nums = [temp] + nums does not work :/ Why?
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
[** Runs a bit slower, but smaller code**]
[*** Removing the if conditions adds in ~15ms more..***]
class Solution:
    def rotate(self, nums, k):
        if k!=0:
            for i in range(k):
                temp = nums[-1]
                del nums[-1]
                nums.insert(0,temp)  #nums = [temp] + nums does not work :/ Why?
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
