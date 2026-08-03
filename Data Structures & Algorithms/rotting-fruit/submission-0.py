class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        t = 0
        fresh_count = 0
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 2:
                    q.append((r, c, t))

                    visited[r][c] = 2
                elif grid[r][c] == 1:
                    fresh_count += 1

        delRow = [-1, 0, 1, 0]
        delCol = [0, +1, 0, -1]

        while q:

            r, c, time = q.popleft()
            t = max(time, t)
            for i in range(4):
                nrow = r + delRow[i]
                ncol = c + delCol[i]

                if (
                    nrow >= 0
                    and ncol >= 0
                    and nrow < rows
                    and ncol < cols
                    and visited[nrow][ncol] != 2
                    and grid[nrow][ncol] == 1
                ):
                    q.append((nrow, ncol, time + 1))
                    visited[nrow][ncol] = 2
                    fresh_count -= 1


        return t if fresh_count == 0 else -1
