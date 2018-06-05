## Problem Statement ##
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.

## My Python3 code ##
from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums):
        return Counter(nums).most_common()[-1][0] ## does not satisfy the note :/ since a new dict is created.
        """
        :type nums: List[int]
        :rtype: int
        """
        

