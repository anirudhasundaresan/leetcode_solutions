#!/home/anirudha/anaconda3/bin/python

## Problem Statement ##

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

## My Python3 code ##

class Solution:
    def isValid(self, s):
        stack = []
        dic = {')':'(','}':'{',']':'['}
        for par in s:
            if par in '({[':
                stack.append(par)
            elif par in ')}]':
                if stack!=[]:
                    if stack[-1] == dic[par]:
                        stack.pop()
                    else:
                        stack.append(par)
                else:
                    return False
        if stack==[]:
            return True
        else:
            return False


        """
        :type s: str
        :rtype: bool
        """

## Smarter solution ## (but takes more time):
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True

        if n % 2 != 0:
            return False

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')

        if s == '':
            return True
        else:
            return False
'''
