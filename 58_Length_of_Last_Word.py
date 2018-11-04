#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
Example:
Input: "Hello World"
Output: 5

## My Python3 code ##
'''

class Solution:
    def lengthOfLastWord(self, s):
        split_s = s.split(" ")
        for i in range(len(split_s)):
            if len(split_s[-1]) == 0:
                del split_s[-1]
        if len(split_s)==0:
            return 0
        return len(split_s[-1])
        """
        :type s: str
        :rtype: int
        """
