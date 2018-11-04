## Problem Statement ##
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:

    Can you solve it in O(N) time and O(1) space?


## My Python3 code ##
class Solution:
    def backspaceCompare(self, S, T):
        stack_S, stack_T = [], []
        for i in S:
            if i =='#': 
                if len(stack_S)!=0:
                    stack_S.pop()
            else:
                stack_S.append(i)
        for i in T:
            if i =='#':
                if len(stack_T)!=0:
                    stack_T.pop()
            else:
                stack_T.append(i)
        if stack_S==stack_T:
            return True
        else:
            return False
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
''' (Better solution using a skip pointer - better because space complexity is O(1))
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
'''
