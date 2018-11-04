#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

## My Python3 code ##
'''

class Solution:
    def judgeCircle(self, moves):
        u = len(moves.split('U'))
        d = len(moves.split('D'))
        l = len(moves.split('L'))
        r = len(moves.split('R'))
        if u==d and l==r:
            return True
        else:
            return False
        """
        :type moves: str
        :rtype: bool
        """
        
# from collections import Counter....one solution that works faster than 92%.
# l = 'UDRLUDRRLSLL' and--> Counter(moves): Counter({'L': 4, 'R': 3, 'U': 2, 'D': 2, 'S': 1}) returns a dictionary....

# Or using map functions: 
# l = map(moves.count, ['R','L','U','D']) and then --> return (l[0]==l[1])&(l[2]==l[3])...in Python2
# In Python3, map object is not subscriptable, hence you have to convert to list and then access elements.

# moves.count('L') will just return int count...easiest
        
