class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i, visited):

            visited[i] = True

            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j, visited)

        n = len(isConnected)
        numOfProvinces = 0
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                dfs(i, visited)
                numOfProvinces += 1

        return numOfProvinces
