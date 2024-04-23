class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        adj = collections.defaultdict(list)
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))
            
        def fn(a):
            dist = [float("inf")] * n
            pq = [(0, a)]
            visited = set()
            curDist = 0
            while pq:
                w, src = heapq.heappop(pq)
                if src in visited:
                    continue
                visited.add(src)
                dist[src] = w
                for des, w1 in adj[src]:
                    if des not in visited:
                        heapq.heappush(pq, (w + w1, des))
            return dist
        
        dist0 = fn(0)
        dist1 = fn(n - 1)
        if dist0[n - 1] == float("inf"): return [False] * len(edges)
        res = []
        for u, v, w in edges:
            res.append(dist0[u] + w + dist1[v] == dist0[n - 1] or dist0[v] + w + dist1[u] == dist0[n - 1])
        return res

        # Algorithm: Dijkstra Algorithm
        # Note: Use Dijkstra to calculate shortest distance from 0 and from n - 1 to all other points. if an edge is
        # in the shortest path, its distance to 0 plus its weight plus its distance to n - 1 should equal to shortest distance from 0 to n - 1.
        # Time complexity: O(2e + eloge) = O(eloge)
        # Space complexity: O(e)