class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n)]

        for i1 in range(n):
            for i2 in range(m):

                if text1[i1] == text2[i2]:
                    dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]
                    continue
                dp[i1][i2] = max(dp[i1][i2 - 1], dp[i1 - 1][i2])

        return dp[n - 1][m - 1]
