class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev = [0] * n

        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue
                up = 0
                left = 0
                if i > 0:
                    up = prev[j]
                if j > 0:
                    left = temp[j - 1]

                temp[j] = up + left
            prev = temp
        return prev[n - 1]
