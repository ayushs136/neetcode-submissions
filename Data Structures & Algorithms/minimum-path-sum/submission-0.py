class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        dp = [[-1] * col for i in range(row)]
        for r in range(row):
            for c in range(col):
                up = float("inf")
                left = float("inf")
                if r == 0 and c == 0:
                    dp[r][c] = grid[r][c]
                    continue

                if r > 0:
                    up = grid[r][c] + dp[r - 1][c]
                if c > 0:
                    left = grid[r][c] + dp[r][c - 1]

                dp[r][c] = min(up, left)

        return dp[row - 1][col - 1]
