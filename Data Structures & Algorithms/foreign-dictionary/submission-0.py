class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # make a dg graph comparing pair of strings:
        # run topo sort

        adj = {char: set() for word in words for char in word}
        indegree = {char: 0 for char in adj}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque([char for char in indegree if indegree[char] == 0])
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return "".join(res) if len(res) == len(indegree) else ""
