#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

Note:
S and J will consist of letters and have length at most 50.
The characters in J are distinct.

## My Python3 code ##
'''

from collections import Counter
# For bigger lists, using Counter is O(n) whereas, list comprehension looping to get the count is O(n^2)
class Solution:
    def numJewelsInStones(self, J, S):
        count = 0
        count_list = Counter(S) # this is a dictionary since the "Counter object is a sub-class of a dictionary"
        for i in J:
             count += count_list[i]
        return count
            
        
        """
        :type J: str
        :type S: str
        :rtype: int
        ANOTHER GOOD SOLUTION: --- 
        count = 0
        for i in J:
            while i in S:
                count += 1
                S = S.replace(i, "", 1) #str.replace(old, new[, max]) --- means replace old substring with new substring with max no. of counts replaced. 
            #print(S)
        return count
        """
