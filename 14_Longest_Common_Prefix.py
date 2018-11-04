#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

## My Python code ##
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs==[]:
            return ""
        min_word = min(strs, key=len)
        print(min_word)
        dic = {}
        for i in range(len(min_word)+1,0,-1):
            if all([True if strss.startswith(min_word[:i]) else False for strss in strs]):
                return min_word[:i]
        return ""

        """
        :type strs: List[str]
        :rtype: str
        """

