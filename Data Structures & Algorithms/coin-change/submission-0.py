class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1] * (amount + 1) for i in range(len(coins))]

        def rec(i, amount):

            if i == 0:
                if amount % coins[0] == 0:
                    return amount / coins[0]
                return float("inf")
            if dp[i][amount] != -1:
                return dp[i][amount]
            notpick = rec(i - 1, amount) 
            pick = float("inf")
            if coins[i] <= amount:
                pick = 1 + rec(i, amount - coins[i])
            dp[i][amount] = min(pick, notpick)
            return dp[i][amount]

        return (
            int(rec(len(coins) - 1, amount)) if rec(len(coins) - 1, amount) != float("inf") else -1
        )
