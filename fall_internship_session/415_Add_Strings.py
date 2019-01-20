#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

## My Python3 code ##
'''

class Solution:
    def addStrings(self, num1, num2):
        length = max(len(num1),len(num2))
        if len(num1)<length:
            num1 = '0'*(length-len(num1)) + num1
        if len(num2)<length:
            num2 = '0'*(length-len(num2)) + num2
        summ = ''
        carry = 0
        for i,j in zip(num1[::-1],num2[::-1]):
            s=int(i)+int(j)+carry
            if s>=10:
                summ+=(str(s-10))
                carry = 1
            else:
                summ+=(str(s))
                carry = 0
        if carry==1:
            return str(carry) + summ[::-1] 
        else:
            return summ[::-1]
            
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
