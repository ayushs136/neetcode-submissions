class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n = len(s)
        m = len(t)
        dp = [[-1] * (m + 1) for _ in range(n)]

        def rec(i, j):

            if j < 0:
                return 1
            if i < 0 and j >= 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = rec(i - 1, j - 1) + rec(i - 1, j)
            else:
                dp[i][j] = rec(i - 1, j)
            return dp[i][j]

        return rec(n - 1, m - 1)
