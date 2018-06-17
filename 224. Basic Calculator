## Problem Statement ##
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

## My Python code ## (VERY VERY HACKY!)
import operator
class Solution(object):
    def result(self, lis):
        # defining a dictionary for ease 
        opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv} # all from the operator module in Python
        i=1 # this code is only for opers in between integers not numbers :/
        if any([True if oper in lis else False for oper in opers]):
            while len(lis)!=1:
                if lis[i] in ['+','-','/','*']:
                    lis[i+1] = opers[lis[i]](int(lis[i-1]),int(lis[i+1]))
                    del lis[i]
                    del lis[i-1]
            return str(lis[0]) 
        else:
            lis = ''.join(lis)
            return lis

            ## assuming all are binary operations
                
    def calculate(self, s):
        lisi = []
        a = [' ','+','-',')','(']
        b = ['',' + ',' - ',' ) ',' ( ']
        for i in range(5):
            s = s.replace(a[i],b[i])
        s = s.split(' ')
        s = [x for x in s if x != '']
        # put artifical brackets in the main string just to make our cases easier
        s = ['('] + s + [')'] 
        stack = []
        for token in s:
            if not token==')':
                stack.append(token)
            else:
                while stack[-1]!='(':
                    lisi.append(stack.pop())
                stack.pop() # to remove an opening bracket
                stack.append(self.result(lisi[::-1]))
            lisi=[]
        return int(stack[0])
                
        
        
        """
        :type s: str
        :rtype: int
        """
        
