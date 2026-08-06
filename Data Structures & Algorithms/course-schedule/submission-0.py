class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        res = []
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            res.append(curr)
            for node in adj[curr]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)

        return len(res) == numCourses
