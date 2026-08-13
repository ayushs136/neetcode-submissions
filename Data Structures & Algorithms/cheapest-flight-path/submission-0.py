class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        adj = [[] for i in range(n)]

        for fro, to, price in flights:
            adj[fro].append((to, price))

        q = deque([(0, src, 0)])  # stops, node, distance
        prices = [float("inf")] * n
        prices[src] = 0
        while q:
            stops, airport, price = q.popleft()

            if stops > k:
                continue

            for next_stop, next_price in adj[airport]:
                new_price = price + next_price

                if prices[next_stop] > new_price:
                    prices[next_stop] = new_price
                    q.append((stops + 1, next_stop, new_price))

        return prices[dst] if prices[dst] != float("inf") else -1
