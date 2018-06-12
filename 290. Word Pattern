## Problem Statement ##
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

## My Python code ##
class Solution(object):
    def wordPattern(self, pattern, str):
        str = str.split(' ')
        if len(str)!=len(pattern):
            return False
        dict = {}
        for i,j in zip(pattern,str):
            if i in dict:
                if dict[i]!=j:
                    return False
            elif j in dict.values():
                return False       
            dict[i]=j
            print(dict)
        return True
            
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
