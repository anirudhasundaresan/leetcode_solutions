#!/home/anirudha/anaconda3/bin/python

## Problem Statement ##
'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

## My Python code ## (one liner: return zip(*collections.Counter(nums).most_common(k))[0])

from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        lis = []
        nums_ctr = Counter.most_common(Counter(nums))
        for i in range(k):
            lis.append(nums_ctr[i][0])
        return lis

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

