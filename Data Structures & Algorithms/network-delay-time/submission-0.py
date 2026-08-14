class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [[] for i in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))

        pq = [(0, k)]  # time, src
        visit = set()
        t = 0
        while pq:
            time, node = heapq.heappop(pq)

            if node in visit:
                continue

            visit.add(node)
            t = max(t, time)

            for nei, wt in adj[node]:
                if nei not in visit:
                    new_time = time + wt
                    heapq.heappush(pq, (new_time, nei))

        return t if len(visit) == n else -1
