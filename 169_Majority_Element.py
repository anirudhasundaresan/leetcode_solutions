#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

## My Python3 code ##

from collections import Counter
class Solution:
    def majorityElement(self, nums):
        return Counter(nums).most_common()[0][0]
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
