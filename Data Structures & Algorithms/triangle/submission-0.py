class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        dp = [[0] * len(triangle[i]) for i in range(n)]

        for c in range(n):
            dp[n - 1][c] = triangle[n - 1][c]

        for r in range(n - 2, -1, -1):
            for c in range(r + 1):
                down = dp[r + 1][c]
                diag = dp[r + 1][c + 1]

                dp[r][c] = triangle[r][c] + min(down, diag)

        return dp[0][0]
