class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1:
                return

            grid[r][c] = 2
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r in [0, rows - 1] or c in [0, cols - 1]):
                    dfs(r, c)
        counter = 0
        print(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    counter += 1
        return counter
