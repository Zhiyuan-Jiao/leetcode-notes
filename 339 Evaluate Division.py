class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, e in enumerate(equations):
            src, des = e
            adj[src].append([des, values[i]])
            adj[des].append([src, 1/values[i]])
        
        def bfs(s, t):
            if s not in adj or t not in adj:
                return -1
            q, visited = collections.deque(), set()
            q.append([s, 1])
            visited.add(s)
            while q:
                n, w = q.popleft()
                if n == t:
                    return w
                for n1, w1 in adj[n]:
                    if n1 not in visited:
                        q.append([n1, w * w1])
                        visited.add(n1)
            return -1
        
        return [bfs(q[0], q[1]) for q in queries]

# Note: a/b * b/c = a/c = 2 * 3 = 6
#         2    3
#       a -> b -> c 
# T: O(n*e) S: O(e)