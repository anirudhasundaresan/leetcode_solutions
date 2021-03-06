#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard.
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

## My Python3 code ##
'''

class Solution:
    def findWords(self, words):
        final = []
        for word in words:
            x=0
            if any(word[0]==r1 for r1 in 'qwertyuiopQWERTYUIOP'):
                for letter in word:
                    for r1 in 'qwertyuiopQWERTYUIOP':
                        if letter==r1:
                            x=x+1
                if x==len(word):
                    final.append(word)

            elif any(word[0]==r2 for r2 in 'asdfghjklASDFGHJKL'):
                for letter in word:
                    for r2 in 'asdfghjklASDFGHJKL':
                        if letter==r2:
                            x=x+1
                if x==len(word):
                    final.append(word)

            else:
                for letter in word:
                    for r3 in 'zxcvbnmZXCVBNM':
                        if letter==r3:
                            x=x+1
                if x==len(word):
                    final.append(word)

        return final

        """
        :type words: List[str]
        :rtype: List[str]
        """


# Better answers:
'''
source = {'up': 'qwertyuiop', 'mi': 'asdfghjkl', 'do': 'zxcvbnm'}
out = []

for word in words:

    if all(letter.lower() in source['up'] for letter in word) or\
        all(letter.lower() in source['mi'] for letter in word) or\
            all(letter.lower() in source['do'] for letter in word):
                out.append(word)
return out
**Need to try using more generators and dictionaries..**
'''
