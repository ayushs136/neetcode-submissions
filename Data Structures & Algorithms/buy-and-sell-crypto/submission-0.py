class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        min_cost = prices[0]
        profit = 0
        for i in range(len(prices)):

            cost = prices[i] - min_cost
            profit = max(profit, cost)
            min_cost = min(min_cost, prices[i])

        return profit
