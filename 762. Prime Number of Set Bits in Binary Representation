## Problem Statement ##
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.
(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)
Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.

## My Python3 code ##
****I did not use the info about the ranges of L,R. If that could be used, we can check for primes only till 1...19.****
*** Hint: Write a helper function to count the number of set bits in a number, then check whether the number of set bits is 2, 3, 5, 7, 11, 13, 17 or 19.***
####NOTE: string.count('1') will give count of element '1' in string..No need to use for loops. 
class Solution:
    def is_prime(self,num):
        if num<2:
            return False
        for i in range(2,num):
            if num%i==0:
                return False
        return True
        
    def countPrimeSetBits(self, L, R):
        primes=0
        for i in range(L,R+1):
            ones=0
            for j in bin(i)[2:]:
                if j=='1':
                    ones = ones + 1
            if self.is_prime(ones):
                primes = primes + 1
        return primes
                
            
        """
        :type L: int
        :type R: int
        :rtype: int
        """
