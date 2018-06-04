## Problem Statement ##

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

## My Python3 code ##

class Solution:
    def hammingDistance(self, x, y):
        count = 0
        for i,j in zip('0'*(31 - len(bin(y)[2:])) + bin(y)[2:], '0'*(31 - len(bin(x)[2:])) + bin(x)[2:]):
            if i!=j:
                count += 1
        return count
        
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
## Kinda stupid...d = bin(x^y) and d.count('1') would have worked faster.
