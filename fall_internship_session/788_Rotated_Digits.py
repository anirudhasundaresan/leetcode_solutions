#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:

    N  will be in range [1, 10000].


## My Python3 code ##
'''
class Solution:
    def rotatedDigits(self, N):
        dic={}
        dic[2]=5
        dic[5]=2
        dic[6]=9
        dic[9]=6
        dic[0]=0
        dic[1]=1
        dic[8]=8
        lis=0
        for i in range(N+1):
            num = list(str(i))
            numb = num.copy()
            for index, digit in enumerate(num):
                if int(digit) in dic:
                    numb[index]=str(dic[int(digit)])
                else:
                    numb[index]='&'
            if numb!=num and numb.count('&')==0:
                lis+=1
        return lis



        """
        :type N: int
        :rtype: int
        """
''' (Much easier!)
class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int  2 5 6 9
        """
        count = 0
        for i in range(1,N+1):
            i = str(i)
            if '3'in i or '4'in i or '7' in i:
                continue
            if '2'in i or '5'in i or '9' in i or '6' in i:
                count +=1
        return count
'''
