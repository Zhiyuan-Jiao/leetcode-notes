class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        srcDes = collections.defaultdict(list)
        for u, v, w in times: 
            srcDes[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        t = 0
        while minHeap:
            w, u = heapq.heappop(minHeap)
            if u in visited: continue
            visited.add(u)
            t = w
            for v, w in srcDes[u]:
                if v not in visited:
                    heapq.heappush(minHeap, (t + w, v))
        return t if len(visited) == n else -1

# Time complexity: O(elogv^2) = O(elogv)
# e = v**2, max number of v in the minHeap is v**2 based on the # of e (it is possible to have bunch of duplicates),
# the pop and push for each v in the minHeap is logv^2, we are going to do # of e this action. 
# Space complexity: O(logv^2) = O(2logv) = O(logv)