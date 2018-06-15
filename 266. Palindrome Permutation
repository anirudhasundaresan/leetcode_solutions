## Problem Statement ##
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true


## My Python3 code ## (Simpler to check: if no. of odds in counter is < 2)
from collections import Counter
class Solution:
    def canPermutePalindrome(self, s):
        s = list(s)
        ctr = 0
        ctr2 = 0
        lis = list(Counter(s).values())
        for i in lis:
            if len(s)%2!=0: 
                if i%2!=0:
                    print(ctr)
                    ctr+=1
            else:
                if i%2!=0:
                    ctr2+=1
        if ctr==1:
            return True
        if ctr!=1 and ctr!=0:
            return False
        if ctr2!=0:
            return False
        else:
            return True
        """
        :type s: str
        :rtype: bool
        """
        
