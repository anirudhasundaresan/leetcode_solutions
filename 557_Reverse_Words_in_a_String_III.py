#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

## My Python code ## (one liner: return " ".join(s[::-1].split(" ")[::-1]))

class Solution(object):
    def reverseWords(self, s):
        lis_split = s.split(' ')
        for i in range(len(lis_split)):
            lis_split[i] = lis_split[i][::-1]
        return ' '.join(lis_split)
        
        """
        :type s: str
        :rtype: str
        """
        
