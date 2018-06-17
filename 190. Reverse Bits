## Problem Statement ##
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?

## My Python code ##
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n_bin = bin(n)[2:]
        n_bin_full = '0'*(32 - len(n_bin)) + n_bin
        return int(n_bin_full[::-1],2)
    # not sure if this is the way to go, or I should focus more on bit manipulation
        
'''
Bit manipulation method: 
def reverseBits(self, n):
        res = 0
        for _ in xrange(32):
            res = (res<<1) + (n&1)
            n>>=1
        return res
'''
