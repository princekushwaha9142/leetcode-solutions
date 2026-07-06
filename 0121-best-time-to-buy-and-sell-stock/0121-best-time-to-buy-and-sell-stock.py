class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        min_price = float("inf")
        n = len(prices)
        for i in range(0, n):
            min_price = min(min_price, prices[i])
            maxprofit = max(maxprofit, prices[i] - min_price)

        return maxprofit