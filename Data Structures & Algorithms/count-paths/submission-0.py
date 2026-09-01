class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def rec(r, c, dp):

            if r == 0 and c == 0:
                return 1

            if r < 0 or c < 0:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            up = rec(r - 1, c, dp)
            left = rec(r, c - 1, dp)
            dp[r][c] = up + left
            return up + left

        dp = [[-1] * n for i in range(m)]
        return rec(m - 1, n - 1, dp)
