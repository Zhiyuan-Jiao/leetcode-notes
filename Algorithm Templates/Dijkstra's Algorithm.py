edges = collections.defaultdict(list)
for u, v, w in times:
    edges[u].append((v, w))

minHeap = [(0, k)]
visited = set()
t = 0

while minHeap:
    w, v = heapq.heappop(minHeap)
    if v in visited:
        continue
    t = w
    visited.add(v)
    for vi, wi in edges[v]:
        heapq.heappush(minHeap, (w + wi, vi))

return t
# Time complexity: O(elogv)
# Space complexity: v