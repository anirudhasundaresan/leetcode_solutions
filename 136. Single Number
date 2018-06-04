## Problem Statement ##
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

## My Python3 code ##

from collections import Counter
class Solution:
    def singleNumber(self, nums):
        return Counter(nums).most_common()[-1][0]
        """
        :type nums: List[int]
        :rtype: int
        """
        ### Or for i in Counter(nums).keys():
                   ##Counter(nums)[i] == 1
                   ##return i
