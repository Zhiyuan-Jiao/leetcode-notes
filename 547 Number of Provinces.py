class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, a):
        # find root
        root = a
        while self.parent[root] != root:
            root = self.parent[root]
        # path compression
        cur = a
        while cur != root:
            parent = self.parent[cur]
            self.parent[cur] = root
            cur = parent
        return root
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if self.rank[ra] >= self.rank[rb]:
            self.parent[rb] = ra
            self.rank[a] += self.rank[b]
        else:
            self.parent[ra] = rb
            self.rank[rb] += self.rank[ra]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        UF = UnionFind(n)
        for r in range(n):
            for c in range(n):
                if r == c or isConnected[r][c] == 0:
                    continue
                UF.union(r, c)
        roots = set()
        for j in range(n):
            roots.add(UF.find(j))
        return len(roots)