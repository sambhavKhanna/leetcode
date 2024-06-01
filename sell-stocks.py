"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    minday = prices[0]
    l = 0
    r = 1
    while r < len(prices):
        if prices[r] < minday:
            minday = prices[r]
            l = r
            r += 1
        else:
            curprof = prices[r] -prices[l]
            profit = max(profit, curprof)
            r += 1
    return profit