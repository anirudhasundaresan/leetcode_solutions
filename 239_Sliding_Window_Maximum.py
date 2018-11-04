#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

## My Python3 code ## Not exacltly linear time since I am splicing..
class Solution:
    def maxSlidingWindow(self, nums, k):
        # need to get sublists first 
        return [max(nums[i:i+k]) for i in range(len(nums)) if i+k-1<len(nums)]
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
''' Better solution since this is in linear time. 
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        list1=nums[:k]
        results=[max(list1)]
        for i in range(k,len(nums)):
            if list1[0]==results[-1]:
                del list1[0]
                list1.append(nums[i])
                results.append(max(list1))
            else:
                del list1[0]
                list1.append(nums[i])
                if nums[i]>results[-1]:
                    results.append(nums[i])
                else:
                    results.append(results[-1])
        return results
'''
        
