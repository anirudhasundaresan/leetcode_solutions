#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''

Given an input string, reverse the string word by word.
Example:  

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.

## My Python code ##
'''

class Solution(object):
    def reverseWords(self, s):
        l=0
        j=0
        lis = []
        for i in range(len(s)):
            if s[i]==" " or s[i]=="":
                l=l+1
        if l==len(s):
            return ""
        s = s.split(" ")
        s = s[::-1]
        for i in range(len(s)):
            if s[i]=='':
                lis.append(i)
        for i in lis:
            del s[i-j]
            j = j + 1
        new_s = " ".join(s)
        return new_s
        """
        :type s: str
        :rtype: str
        """
        
