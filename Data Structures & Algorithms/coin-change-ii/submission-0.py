class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]

        def f(i, target):

            if i == 0:
                return 1 if target % coins[i] == 0 else 0
            if dp[i][target] != -1:
                return dp[i][target]
            not_take = f(i - 1, target)
            take = 0

            if coins[i] <= target:
                take = f(i, target - coins[i])

            dp[i][target] = take + not_take
            return dp[i][target]

        return f(n - 1, amount)
