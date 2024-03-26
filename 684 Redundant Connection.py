class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(a):
            # find root
            cur = a
            while parent[cur] != cur:
                cur = parent[cur]
            root = cur
            # path compression
            cur = a
            while parent[cur] != root:
                cparent = parent[cur]
                parent[cur] = root
                cur = cparent
            return root
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] >= rank[rb]:
                parent[rb] = ra
                rank[ra] += rank[rb]
            else:
                parent[ra] = rb
                rank[rb] += rank[ra]
            return True
        
        for a, b in edges:
            if not union(a, b): return [a, b]

# Note: Union node when there is an edge, if roots are the same for two node mean they are already connected in before and this is the redundant edge
# Time complexity: O(n)
# Space complexity: O(n)
