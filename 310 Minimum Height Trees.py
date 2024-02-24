class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        # create graph
        edge = [set() for i in range(n)]
        for l, r in edges:
            edge[l].add(r)
            edge[r].add(l)
        
        # add all node at the node with only one edge to queue
        q = collections.deque()
        for i in range(n):
            if len(edge[i]) == 1: q.append(i)
        
        # bfs to remove nodes layer by layer
        # append the last layer to response
        res = []
        while q:
            res = list(q)
            for j in range(len(q)):
                node = q.popleft()

                for n in edge[node]:
                    edge[n].remove(node)
                    if len(edge[n]) == 1: q.append(n)
        return res

# Time complexity: O(n)
# Space complexity: O(n)