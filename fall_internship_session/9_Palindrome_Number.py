#!/home/anirudha/anaconda3/bin/python

## Problem Statement ##

'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

## My Python3 code ##

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        if x==x[::-1]:
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool

        """
'''
### Without using string, but this consumes a list memory..###
# Taking each digit and storing into list.
class Solution:
    def isPalindrome(self, x):
        lis = []
        if x<0:
            return False
        while x:
            lis.append(x%10)
            x = x//10
        if lis==lis[::-1]:
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool
        """
'''

