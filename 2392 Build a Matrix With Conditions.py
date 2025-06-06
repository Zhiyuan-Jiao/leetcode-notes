class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(node, adj, visited, path, order):
            if node in path: return False
            if node in visited: return True
            path.add(node)
            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei, adj, visited, path, order): return False
            path.remove(node)
            order.append(node)
            return True

        def topoSort(edges):
            adj = defaultdict(list)
            for src, dst in edges:
                adj[src].append(dst)
            visited, path = set(), set()
            order = []
            for src in range(1, k + 1):
                if src not in visited:
                    if not dfs(src, adj, visited, path, order): return []
            return order[::-1]

        rowOrder = topoSort(rowConditions)
        colOrder = topoSort(colConditions)
        if not rowOrder or not colOrder: return []
        rowOrder = {n:i for i, n in enumerate(rowOrder)}
        colOrder = {n:i for i, n in enumerate(colOrder)}

        res = [[0] * k for j in range(k)]
        for num in range(1, k + 1):
            r, c = rowOrder[num], colOrder[num]
            res[r][c] = num
        return res