#Question: Best time to buy and sell stocks
#pattern: greedy 

# Approch 
# Track the minimum price seen so far and
#  compute profit at each step. Update the maximum profit by 
# comparing current profit with the best seen so far.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_profit=0

        for price in prices:
            if price<min_price:
                min_price=price
            profit =price-min_price

            if profit >max_profit:
                max_profit=profit
        return max_profit