class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return
            grid[r][c] = "0"

            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r - 1, c)

        rows, cols = len(grid), len(grid[0])

        numOfIsland = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c)
                    numOfIsland += 1
        return numOfIsland
