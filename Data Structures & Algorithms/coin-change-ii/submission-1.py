class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        for target in range(amount + 1):
            if target % coins[0] == 0:
                dp[0][target] = 1

        for i in range(1, n):
            for target in range(amount + 1):
                not_take = dp[i - 1][target]
                take = 0

                if coins[i] <= target:
                    take = dp[i][target - coins[i]]

                dp[i][target] = take + not_take

        return dp[n - 1][amount]
