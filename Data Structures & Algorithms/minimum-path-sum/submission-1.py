class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        prev = [float("inf")] * col
        for r in range(row):
            curr = [0] * col
            for c in range(col):
                if r == 0 and c == 0:
                    curr[c] = grid[r][c]
                    continue

                up = prev[c]
                left = curr[c - 1] if c > 0 else float("inf")
                curr[c] = grid[r][c] + min(up, left)
            prev = curr

        return prev[col - 1]
