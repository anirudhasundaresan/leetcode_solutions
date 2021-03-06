#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

## My Python3 code ##
'''
class Solution(object):
    def peakIndexInMountainArray(self, A):
        # There can be many variations of O(n), but strive for a O(log n) using binary search.
        low = 0
        high = len(A)-1
        mid = (low+high)//2
        print(mid)
        while high-low>0: 
            if A[mid-1]<A[mid] and A[mid]>A[mid+1]:
                return mid
            elif A[mid-1]<A[mid]<A[mid+1]:
                low = mid
            elif A[mid-1]>A[mid]>A[mid+1]:
                high = mid
            mid = (low+high)//2
            if mid==low:
                mid = low+1
                break
        """
        :type A: List[int]
        :rtype: int
        """
