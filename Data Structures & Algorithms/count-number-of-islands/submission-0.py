class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j, visited, grid):
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or visited[i][j]
                or grid[i][j] == "0"
            ):
                return
            visited[i][j] = True

            dfs(i, j + 1, visited, grid)
            dfs(i + 1, j, visited, grid)
            dfs(i, j - 1, visited, grid)
            dfs(i - 1, j, visited, grid)

        rows, cols = len(grid), len(grid[0])

        numOfIsland = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c, visited, grid)
                    numOfIsland += 1
        return numOfIsland
