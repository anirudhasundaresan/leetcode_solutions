#!/home/anirudha/anaconda3/bin/python

## Problem Statement ##

'''
 Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:

    Each element in the result must be unique.
    The result can be in any order.
'''

## My Python3 code ##

class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2))) ## Or use '&'
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

