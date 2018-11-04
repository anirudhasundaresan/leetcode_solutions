## Problem Statement ##
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

## My Python3 code ##
# Here, an non-general approach would be to use the set int loop[8] = {4,16,37,58,89,145,42,20}; since all un-happy numbers apparently fall in this range.
class Solution:
    def isHappy(self, n):
        new_n = list(str(n)) # str(n) is enough since we are using for i in new_n...
        # Also, many solutions have used set instead of list because 'in' operation in set is avg: O(1), whereas for list, it is O(n) on an avg.
        lis = [] # lis = set() and NOT lis = ()
        lis.append(n)
        if n==1:
            return True
        while True:
            cond = sum([int(i)**2 for i in new_n])
            if cond in lis:
                return False
            lis.append(cond)
            new_n = list(str(cond))
            if cond==1:
                return True
            
            print(lis)

        
    
        """
        :type n: int
        :rtype: bool
        """
        
