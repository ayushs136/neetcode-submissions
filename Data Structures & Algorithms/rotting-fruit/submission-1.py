class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        freshCount, t = 0, 0
        delRows = [-1, 0, 1, 0]
        delCols = [0, 1, 0, -1]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, t))
                    visited[r][c] = 2
                elif grid[r][c] == 1:
                    freshCount += 1

        while q:
            r, c, time = q.popleft()
            t = max(time, t)

            for i in range(4):
                nrow = r + delRows[i]
                ncol = c + delCols[i]

                if (
                    nrow >= 0
                    and nrow < rows
                    and ncol >= 0
                    and ncol < cols
                    and visited[nrow][ncol] != 2
                    and grid[nrow][ncol] == 1
                ):
                    q.append((nrow, ncol, time + 1))
                    visited[nrow][ncol] = 2
                    freshCount -= 1

        return t if freshCount == 0 else -1
