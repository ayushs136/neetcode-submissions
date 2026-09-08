class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        def f(i, target):

            if i == 0:
                if target % coins[i] == 0:
                    return target // coins[i]
                else:
                    return float("inf")
            if dp[i][target] != -1:
                return dp[i][target]
            not_take = f(i - 1, target)
            take = float("inf")

            if coins[i] <= target:
                take = 1 + f(i, target - coins[i])

            dp[i][target] = min(take, not_take)
            return dp[i][target]

        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]

        for amt in range(amount + 1):
            if amt % coins[0] == 0:
                dp[0][amt] = amt // coins[0]
            else:
                dp[0][amt] = float("inf")

        for i in range(1, n):

            for target in range(amount + 1):

                not_take = dp[i - 1][target]
                take = float("inf")

                if coins[i] <= target:
                    take = 1 + dp[i][target - coins[i]]

                dp[i][target] = min(take, not_take)

        return dp[n - 1][amount] if dp[n - 1][amount] != float("inf") else -1
