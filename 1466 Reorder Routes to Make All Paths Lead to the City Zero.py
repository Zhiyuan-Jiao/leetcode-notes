class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        toCityN, fromCityN, visited, res = defaultdict(list), defaultdict(list), set(), 0

        # build the tree
        for a, b in connections:
            toCityN[b].append(a)
            fromCityN[a].append(b)
        
        # bfs from city 0
        q = deque([0])
        while q:
            city = q.popleft()
            visited.add(city)
            for nc in toCityN[city]:
                if nc not in visited:
                    q.append(nc)
            for mc in fromCityN[city]:
                if mc not in visited:
                    q.append(mc)
                    res += 1
        return res
            