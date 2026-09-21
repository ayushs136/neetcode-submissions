class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        ahead_buy = 0
        ahead_not_buy = 0

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                if buy:
                    curr_buy = max(-prices[i] + ahead_not_buy, ahead_buy)
                else:
                    curr_not_buy = max(prices[i] + ahead_buy, ahead_not_buy)
            ahead_not_buy = curr_not_buy
            ahead_buy = curr_buy

        return ahead_buy
