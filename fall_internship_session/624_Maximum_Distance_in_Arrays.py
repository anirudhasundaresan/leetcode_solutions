#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
 Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:

Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Note:

    Each given array will have at least 1 number. There will be at least two non-empty arrays.
    The total number of the integers in all the m arrays will be in the range of [2, 10000].
    The integers in the m arrays will be in the range of [-10000, 10000].

## My Python3 code ## [code is not good, it's at the end of the spectrum; copying costs O(n)]
'''
import numpy as np
class Solution:
    def maxDistance(self, arrays):
        lmax, lmin = [], []
        for lis in arrays:
            lmin.append(lis[0])
            lmax.append(lis[-1])
        if lmax.index(max(lmax)) == lmin.index(min(lmin)):
            l = lmin.copy()
            l.remove(min(lmin))
            a = max(lmax) - min(l)
            l = lmax.copy()
            l.remove(max(lmax))
            b = max(l) - min(lmin)
            if a>b: 
                return a 
            else: 
                return b
        else:
            return max(lmax) - min(lmin)            
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
## Better solution:...
'''
class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        if not arrays or len(arrays) < 2:
            return 0
        
        res, tempmin, tempmax = abs(arrays[0][0] - arrays[1][-1]), arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            subarray = arrays[i]
            res = max(res, max(abs(tempmin - subarray[-1]), abs(tempmax - subarray[0])))
            tempmin = min(subarray[0], tempmin)
            tempmax = max(subarray[-1], tempmax)
        return res
'''
