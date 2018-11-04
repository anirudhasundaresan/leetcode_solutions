#!/home/anirudha/anaconda3/bin:/home/anirudha/bin
## Problem Statement ##
Implement an iterator to flatten a 2d vector.

Example:

Input: 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]
Output: [1,2,3,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,2,3,4,5,6].
             
## My Python code ##
class Vector2D(object):

''' # for the first function, it is faster
        self.data = []
        for v in vec2d[::-1]:
            self.data += v[::-1]
'''

    def __init__(self, vec2d):
        self.lis = []
        # append would have used the [] brackets as well. Thus, use extend
        for i in vec2d:
            self.lis.extend(i)
        self.lis = self.lis[::-1]
        # list reversal time is O(N), but better to reverse and then call next as then you will need multiple O(1) from pops. 
        # If no reversal now, pop will take O(N) since it is pop(0)
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        

    def next(self):
        return self.lis.pop()
        """
        :rtype: int
        """
        

    def hasNext(self):
        if len(self.lis)!=0:
            return True
        else:
            return False
        """
        :rtype: bool
        """
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
