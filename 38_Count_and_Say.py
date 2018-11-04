#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

## My Python3 code ## (learnt the usage of groupby in itertools, looked at hints)
'''

from itertools import groupby
class Solution:
    def countAndSay(self, n):
        def rec_str(stri, ct):
            if ct==n:
                return stri
            stri2 =''
            total_lists = [list(g) for k,g in groupby(list(stri))            ]
            for i in total_lists:
                stri2+= str(len(i)) + str(i[0])
            ct+=1
            print("number ", ct, ": ", stri2 )
            return rec_str(stri2, ct)
        return rec_str('1', 1)
        
        
        """
        :type n: int
        :rtype: str
        """
        
