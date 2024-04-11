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

# Note: To Calculate min cost to connect all points
# Similar to Dijkstra's Algorithm, but dont need to cummulate weight for each push into the heap.
# Time complexity: O(nlogn^2) = O(nlogn)
# Space complexity: O(n^2)