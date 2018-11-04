#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

## My Python3 code ##
'''
class Solution:
    def countBits(self, num):
        lis = []
        for no in range(num+1):
            lis.append(bin(no)[2:].count('1'))
        return lis
            
        """
        :type num: int
        :rtype: List[int]
        """
''' (More creative solution)
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        while len(ans) < num + 1:
            ans += [1 + x for x in ans]
        # len(ans) > num
        return ans[:num+1]
'''
