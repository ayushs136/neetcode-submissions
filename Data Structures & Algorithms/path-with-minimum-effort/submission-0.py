class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        row, col = len(heights), len(heights[0])

        minHeap = [(0, 0, 0)]  # diff,  r, c,

        visited = set()
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if (r, c) == (row - 1, col - 1):
                return diff

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr == row or nc < 0 or nc == col or (nr, nc) in visited:
                    continue

                newDiff = max(diff, abs(heights[nr][nc] - heights[r][c]))
                heapq.heappush(minHeap, (newDiff, nr, nc))
