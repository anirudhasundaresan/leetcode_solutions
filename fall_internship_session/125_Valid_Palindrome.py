#!/home/anirudha/anaconda3/bin/python

## Problem Statement ##
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

## My Python3 code ##

class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        print(s)
        for i in s:
            if not i.isalnum():
                s = s.replace(i, ' ') # this is the way to remove a character from a string.
        print(s)
        s = s.replace(' ','')
        if s==s[::-1]:
            return True
        else:
            return False


        """
        :type s: str
        :rtype: bool
        """

