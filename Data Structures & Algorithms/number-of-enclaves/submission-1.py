class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r in [0, rows - 1] or c in [0, cols - 1]):
                    q.append((r, c))
                    grid[r][c] = 2

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0 <= nc < cols) and grid[nr][nc] == 1:
                    q.append((nr, nc))
                    grid[nr][nc] = 2

        counter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    counter += 1
        return counter
