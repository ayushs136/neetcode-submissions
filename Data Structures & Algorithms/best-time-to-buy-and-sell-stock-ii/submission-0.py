class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[-1] * (2) for _ in range(n)]

        def f(i, buy):
            if i == n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            if buy:
                dp[i][buy] = max(-prices[i] + f(i + 1, False), f(i + 1, True))
            else:
                dp[i][buy] = max(prices[i] + f(i + 1, True), f(i + 1, False))

            return dp[i][buy]

        return f(0, True)
