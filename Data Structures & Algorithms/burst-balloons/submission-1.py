class Solution:
    def maxCoins(self, nums: list[int]) -> int:

        nums = [1] + nums + [1]
        m = len(nums)
        dp = [[0] * m for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(i, m):
                for k in range(i + 1, j):
                    coins = nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]

                    dp[i][j] = max(dp[i][j], coins)
        return dp[0][m - 1]
