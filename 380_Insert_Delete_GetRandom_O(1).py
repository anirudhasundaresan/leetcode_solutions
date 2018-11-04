#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

## My Python3 code ##
class RandomizedSet:

    def __init__(self):
        self.dic = {}
        """
        Initialize your data structure here.
        """
        

    def insert(self, val):
        if val in self.dic:
            return False
        else:
            self.dic[val] = val
            return True
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        

    def remove(self, val):
        if val not in self.dic:
            return False
        else:
            del self.dic[val] # remember the del command 
            return True
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        return random.choice(list(self.dic.keys())) # remember this; d.keys() is an iterator in py3, hence you need to list()
        """
        Get a random element from the set.
        :rtype: int
        """
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
