class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1] * (m + 1) for _ in range(n)]

        def rec(i1, i2):
            if i1 < 0 or i2 < 0:
                return 0
            if dp[i1][i2] != -1:
                return dp[i1][i2]
            if text1[i1] == text2[i2]:
                return 1 + rec(i1 - 1, i2 - 1)
            dp[i1][i2] = max(rec(i1, i2 - 1), rec(i1 - 1, i2))
            return dp[i1][i2]

        return rec(n - 1, m - 1)
