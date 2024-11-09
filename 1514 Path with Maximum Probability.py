class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Dijkstra
        # graph = defaultdict(list)
        # for i, e in enumerate(edges):
        #     graph[e[0]].append((e[1], succProb[i]))
        #     graph[e[1]].append((e[0], succProb[i]))

        # q = [(1, start_node)]
        # visited = set()
        # while q:
        #     prob, node = heapq.heappop(q)
        #     if node in visited: continue
        #     if node == end_node:
        #         return -prob
        #     visited.add(node)
        #     for n1, p1 in graph[node]:
        #         heapq.heappush(q, (-abs(p1 * prob), n1))
        # return 0.0

        # Bellman Ford
        probs = [float("-inf")] * n
        probs[start_node] = 1
        for i in range(n - 1):
            temp = probs.copy()
            for j, e in enumerate(edges):
                n1, n2 = e
                temp[n1] = max(temp[n1], probs[n2] * succProb[j])
                temp[n2] = max(temp[n2], probs[n1] * succProb[j])
            probs = temp
        return probs[end_node] if probs[end_node] != float("-inf") else 0.0
        