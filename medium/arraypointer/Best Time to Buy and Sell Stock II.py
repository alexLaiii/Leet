"""
Think of yourself as a stock daytrader with superpower to look at the stock market of tmr (and only tmr), where your superpower only last len(prices) days
Note that you are allow to sell and buy the stock again in the same day (no cooldown)
So you always buy stock whenever theres a profit (stock prices of tmr is higher than today). 
No matter how small or how big the profit is, because you are guarantee to win
When theres no profit (stock prices of tmr is lower than today), you dont do anything, because it is gurantee lost
This approach guranteen the sum of the profit equals to the maximum profit after len(prices) days
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                max_profit += prices[i+1] - prices[i]
            
        return max_profit
        
  
