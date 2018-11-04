#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.

## My Python3 code ## (intermediate conversion to string might delay...always better to check conditions with int itself)
## The // does integer division by a power of ten to move the digit to the ones position, then the % gets the remainder after division by 10.

class Solution:
    def selfDividingNumbers(self, left, right):
        ls = []
        for nums in range(left, right+1):
            num_str = str(nums)
            if num_str.count('0')>=1:
                continue
            count = 0
            for dig in num_str:
                if nums%int(dig)==0:
                    count += 1
            if count==len(num_str):
                ls.append(nums)
        return ls
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
