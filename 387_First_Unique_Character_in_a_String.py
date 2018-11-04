#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem statement ##
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


## My Python3 code ## 
# My code does a single pass through the array and uses stack
# Other solutions use 'chr', 'ord', s.find and s.rfind - (https://docs.python.org/3/library/functions.html)
ord('a') returns 97 and chr(97) returns 'a' (string return) -- raises ValueError if not in range (useful for try..except)
'''
str1 = "this is really a string example....wow!!!";
str2 = "is";
# find returns first index and rfind returns last index. Both return -1 if not found. 
print str1.rfind(str2) - 5
print str1.rfind(str2, 0, 10) - 5
print str1.rfind(str2, 10, 0) - -1

print str1.find(str2) - 2
print str1.find(str2, 0, 10) - 2
print str1.find(str2, 10, 0)- -1
'''

class Solution:
    def firstUniqChar(self, s):
        if len(s)==0:
            return -1
        stack = []
        i = 0
        for letter in s:
            if letter in s[i+1:]: #splicing is O(k)
                stack.append(letter)
                i+=1
            elif letter in stack:
                i+=1
            else:
                return i
        return -1
                
        
        ''' (time limit exceeded)
        i = 0
        for letter in s:
            if s.count(letter)==1:
                return i 
            else:
                i+=1
        return -1
        '''
        """
        :type s: str
        :rtype: int
        """
