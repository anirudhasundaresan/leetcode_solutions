#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

## My Python3 code ## [or you can compare the count of ransomnote values]
class Solution:
    def canConstruct(self, ransomNote, magazine):
        magazine = list(magazine)
        for i in ransomNote:
            try:
                magazine.remove(i)
            except ValueError:
                return False
        return True
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
