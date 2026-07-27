class Solution(object):
    def maxProfit(self, prices):
        min_price=float('inf')
        max_profit=0

        for i in prices:
            min_price=min(min_price,i)
            profit=i-min_price
            max_profit=max(max_profit,profit)
        return max_profit
      
        