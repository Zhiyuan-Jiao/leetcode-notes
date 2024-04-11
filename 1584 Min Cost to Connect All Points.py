class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = [[] for i in range(len(points))]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                manDis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges[i].append((j, manDis))
                edges[j].append((i, manDis))
        
        minHeap = [(0, 0)]
        visited = set()
        res = 0
        while len(visited) < len(points):
            w, n = heapq.heappop(minHeap)
            if n in visited: continue
            visited.add(n)
            res += w
            for n1, w1 in edges[n]:
                if n1 not in visited:
                    heapq.heappush(minHeap, (w1, n1))
        return res

# Note: Prim's Algorithm
# Similar to Dijkstra's Algorithm, but dont need to cummulate 
# weight for each push into the heap.
# Time complexity: O(n^2 + nlogn^2) = O(n^2 + nlogn)
# Space complexity: O(n^2)