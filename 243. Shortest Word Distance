## Problem Statement ##
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3

Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


## My Python3 code ##

import numpy as np 
class Solution:
    def shortestDistance(self, words, word1, word2):
        min_ = np.inf
        word1_ind, word2_ind = [], []
        for index, word in enumerate(words):
            if word==word1:
                word1_ind.append(index)
            elif word==word2:
                word2_ind.append(index)
        for i in word1_ind:
            for j in word2_ind:
                min_ = min(abs(i-j),min_)
        return min_        
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
''' (Another method using dictionary)
        dic ={}
        distance = len(words)
        for i, word in enumerate(words):
            if word == word1:
                if word2 in dic:
                    distance = min(distance, i - dic[word2])
                dic[word1] = i
            elif word == word2:
                if word1 in dic:
                    distance = min(distance, i - dic[word1])
                dic[word2] = i
        return distance
'''
