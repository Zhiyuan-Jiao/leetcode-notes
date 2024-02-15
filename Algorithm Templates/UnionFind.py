class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        # Find root
        root = n
        while self.parent[root] != root:
            root = self.parent[root]
        # Path compression (add node directly to root)
        if n != root:
            while self.parent[n] != root:
                parent = self.parent[n]
                self.parent[n] = root
                n = parent
        return root
    
    def Union(self, n, m):
        rn, rm = self.find(n), self.find(m)
        
        if self.rank[rn] >= self.rank[rm]:
            self.parent[rm] = rn
            self.rank[rn] += self.rank[rm]
        else:
            self.parent[rn] = rm
            self.rank[rm] += self.rank[rn]
        return True
        

node = UnionFind(10)
node.Union(1, 2)
node.Union(1, 3)
node.Union(3, 4)
node.Union(7, 8)
print(node.find(9))