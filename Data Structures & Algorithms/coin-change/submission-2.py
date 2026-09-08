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
        prev = [0] * (amount + 1)

        for amt in range(amount + 1):
            if amt % coins[0] == 0:
                prev[amt] = amt // coins[0]
            else:
                prev[amt] = float("inf")

        for i in range(1, n):
            curr = [0]*(amount+1)

            for target in range(amount + 1):

                not_take = prev[target]
                take = float("inf")

                if coins[i] <= target:
                    take = 1 + curr[target - coins[i]]

                curr[target] = min(take, not_take)
            prev = curr
        return prev[amount] if prev[amount] != float("inf") else -1
