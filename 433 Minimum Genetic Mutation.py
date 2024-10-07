class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        def isMutation(a, b):
            differences = 0
            for i in range(8):
                if a[i] != b[i]:
                    differences += 1
                if differences > 1: return False
            return True

        q = collections.deque() # (gene string, number of mutations)
        q.append((startGene, 0)) 
        visited = set()

        while q:
            cur_gene, mutations = q.popleft()
            if cur_gene == endGene: return mutations
            for gene in bank:
                if gene not in visited and isMutation(cur_gene, gene):
                    q.append((gene, mutations + 1))
                    visited.add(gene)
        return -1

# T: O(n), S: O(n)
# Note: Bfs find shortest path