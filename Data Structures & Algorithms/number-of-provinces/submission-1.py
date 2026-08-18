class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def findParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])

        return self.parent[node]

    def unionByRank(self, u, v):
        p1, p2 = self.findParent(u), self.findParent(v)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.components -= 1
        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        dsu = DisjointSet(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:

                    dsu.unionByRank(i, j)

        return dsu.components
