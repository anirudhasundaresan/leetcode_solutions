#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

## My Python3 code ## (not a good solution)
'''
## Better solution is to create a new list called min_stack and whenever x < min_stack[-1], append x onto min_stack.
## This way, during function call, only min_stack[-1] need to be returned.

import numpy as np
class MinStack:
    mini = np.inf
    def __init__(self):
        self.stack = []
        """
        initialize your data structure here.
        """

    def push(self, x):
        self.stack.append(x)
        if x<=mini:
            mini = x
        """
        :type x: int
        :rtype: void
        """

    def pop(self):
        self.stack.pop()
        """
        :rtype: void
        """

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """

    def getMin(self):
        return mini
        """
        :rtype: int
        """

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
