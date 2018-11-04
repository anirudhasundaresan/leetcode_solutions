## Problem Statement ##
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.



## My Python3 code #3 (good solution: O(n))
class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        cp, sp = prices[0], prices[0] 
        profit = 0 
        for price in prices[1:]:
            if price > cp:
                sp = max(sp, price)
            elif price < cp:
                cp = price
                sp = price
            profit = max(profit, (sp-cp))
        return profit        
        """
        :type prices: List[int]
        :rtype: int
        """
        
