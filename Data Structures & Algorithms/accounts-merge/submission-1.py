class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)

        if p1 == p2:
            return False

        if self.size[p1] > self.size[p2]:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DisjointSet(len(accounts))
        emailToIndex = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToIndex:
                    dsu.union(i, emailToIndex[e])
                else:
                    emailToIndex[e] = i

        emailGroup = defaultdict(list)

        for e, i in emailToIndex.items():
            leader = dsu.find(i)
            emailGroup[leader].append(e)

        res = []
        for i, eList in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(eList))

        return res
