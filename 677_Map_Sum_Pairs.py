#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5

## My Python3 code ## [Naturally this must make you think of dictionaries, not 2 separate lists..]
class MapSum(object):

    def __init__(self):
        self.key_list = []
        self.data_list = []
        """
        Initialize your data structure here.
        """
        

    def insert(self, key, val):
        if key in self.key_list:
            self.data_list[self.key_list.index(key)] = val
        else:
            self.key_list.append(key)
            self.data_list.append(val)
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        

    def sum(self, prefix):
        summ=0
        for index, keys in enumerate(self.key_list):
            if keys.startswith(prefix):
                summ+=self.data_list[index]
        return summ
        """
        :type prefix: str
        :rtype: int
        """
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
