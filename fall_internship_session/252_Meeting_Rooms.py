#!/home/anirudha/anaconda3/bin/python

## Problem Statement ##
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
'''

## My Python3 code ##

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def sort_func(obj):
    return obj.start

class Solution:  ### Best solution has done start end comparison.
    def canAttendMeetings(self, intervals):
        lis = []
        intervals = sorted(intervals, key = sort_func)
        for i in intervals:
            lis.append(i.start)
            lis.append(i.end)
        if lis == sorted(lis):
            return True
        else:
            return False


        """
        :type intervals: List[Interval]
        :rtype: bool
        """

## Also, instead of creating a new function, it would be better to use lambda function.
## intervals.sort(key = lambda x: x.start)
